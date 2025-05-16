#pragma once
#include "AiMaker/precompiledheader.hpp"
#include "AiMaker/Interface.hpp"
#include <fstream>

// spacing between matches; must match the value in AutoMatch.py
constexpr int32 match_spacing = 24*2;
// maximum number of match rows
constexpr int32 max_rows = 11;
// maximum number of match columns
constexpr int32 max_cols = max_rows;
// maximum number of units on map
constexpr int32 max_units = 2000;

class AutoMatch
{
public:

    // micro for each match/player; not used yet
    enum MicroType
    {
        NONE, // patrol
        BUILTIN, // patrol + hit-and-run, avoid-projectiles
        IMMORTAL, // immortal micro
    };

    // match status
    enum Status
    {
        INVALID = -1,
        UNKNOWN = 0,
        READY,
        RUNNING,
        COMPLETED,
        WRITTEN,
    };

    // data for a single match
    struct Match
    {
        Var unitId = 0;
        Var hpInitial = 0;
        Var hpFinal = 0;
        Var unitCount = 0;
        Var eunitId = 0;
        Var ehpInitial = 0;
        Var ehpFinal = 0;
        Var eunitCount = 0;
        // Var microType = 0;
        // Var emicroType = 0;
        Var status = 0;
    };

    // number of Vars needed to store the data
    static constexpr int sizeMatch = sizeof(Match)/sizeof(Var);
    // data for all matches
    Array matchData{sizeMatch*max_rows*max_cols, 0};
    // data for current match
    Match match;

    void run()
    {
        // disable town-size
        SN[SnID::MINIMUM_TOWN_SIZE] = 0;
        SN[SnID::MAXIMUM_TOWN_SIZE] = 0;
        SN[SnID::SAFE_TOWN_SIZE] = 0;
        SN[SnID::SENTRY_DISTANCE] = 0;
        SN[SnID::TARGET_PLAYER] = 0;
        SN[SnID::ENEMY_SIGHTED_RESPONSE_DISTANCE] = 0;
        SN[SnID::NUMBER_ATTACK_GROUPS] = 0;
        SN[SnID::ENABLE_PATROL_ATTACK] = false;

        // disable explorers
        SN[SnID::NUMBER_EXPLORE_GROUPS] = 0;
        SN[SnID::NUMBER_BOAT_EXPLORE_GROUPS] = 0;
        SN[SnID::PERCENT_CIVILIAN_EXPLORERS] = 0;
        SN[SnID::CAP_CIVILIAN_EXPLORERS] = 0;
        SN[SnID::INITIAL_EXPLORATION_REQUIRED] = 0;
        SN[SnID::TOTAL_NUMBER_EXPLORERS] = 0;
        
        // disable built-in micro
        setAutoMaintainDistancePercent(0);
        setAutoDodgeMisslesPercent(0);

        // are all the matches done?
        BoolVar allDone = true;

        // loop over each match
        begin_for(Var i=0, i<max_rows*max_cols, i += 1);
        {
            Var j = i-1; // work-around for for-loop bug
            
            // load match data ; skip rest if match is invalid
            match.status = matchData.get(j*sizeMatch+8);
            begin_if(match.status == Status::INVALID || match.status == Status::COMPLETED);
            continue_loop();
            end_if();
            match.unitId     = matchData.get(j*sizeMatch+0);
            match.hpInitial  = matchData.get(j*sizeMatch+1);
            match.hpFinal    = matchData.get(j*sizeMatch+2);
            match.unitCount  = matchData.get(j*sizeMatch+3);
            match.eunitId    = matchData.get(j*sizeMatch+4);
            match.ehpInitial = matchData.get(j*sizeMatch+5);
            match.ehpFinal   = matchData.get(j*sizeMatch+6);
            match.eunitCount = matchData.get(j*sizeMatch+7);

            // if we got here then at least one match is running
            allDone = false;

            // define match position
            Var y = divideFloor(j, max_cols); Var x = j % max_cols;
            Var xMin = x*match_spacing;
            Var yMin = y*match_spacing;
            Var xMax = xMin + (match_spacing-1);
            Var yMax = yMin + (match_spacing-1);
            Var xAve = xMin + (match_spacing/4);
            Var yAve = yMin + (match_spacing/4);

            // find relevant units

            DUC::clearFiltersAndLists();
            Point tmp; tmp.y = yAve; tmp.x = xAve; // work-around for DE point bug
            DUC::setTargetingPoint(tmp);
            
            Var id = 0;
            begin_while(id <= max_units); // id loop
            {
                begin_if(CurrObj::checkData(ObjData::DISTANCE) <= (match_spacing/2)
                        && CurrObj::checkData(ObjData::CATEGORY) == Category::COMBATANT 
                        && CurrObj::checkData(ObjData::HITPOINTS) > 0 
                        && CurrObj::setAndCheckExists(id));
                {
                    DUC::localList::add(id);
                }
                end_if();
                id += 1;
            }
            end_while();

            DUC::localList::remove(ObjData::POINT_X, CompareOp::LESS_THAN, xMin);
            DUC::localList::remove(ObjData::POINT_X, CompareOp::GREATER_THAN, xMax);
            DUC::localList::remove(ObjData::POINT_Y, CompareOp::LESS_THAN, yMin);
            DUC::localList::remove(ObjData::POINT_Y, CompareOp::GREATER_THAN, yMax);
            DUC::remoteList::copyFromLocalList();
            DUC::remoteList::remove(ObjData::PLAYER, CompareOp::EQUAL, PlayerID::SELF);
            DUC::localList::remove(ObjData::PLAYER, CompareOp::NOT_EQUAL, PlayerID::SELF);

            // initialize match status

            begin_if(match.status == Status::UNKNOWN);
            {
                begin_if(DUC::localList::notEmpty() && DUC::remoteList::notEmpty());
                match.status = Status::READY;
                begin_else();
                match.status = Status::INVALID; 
                end_if();
            }
            end_if();
            
            // get initial data

            begin_if(match.status == Status::READY);
            {
                // local data
                match.hpInitial = DUC::localList::getSum(ObjData::MAXHP);
                CurrObj::setFromList(SearchSource::LOCAL, 0);
                match.unitId = CurrObj::get(ObjData::BASE_TYPE);
                match.unitCount = DUC::localList::size();

                // remote data
                match.ehpInitial = DUC::remoteList::getSum(ObjData::MAXHP);
                CurrObj::setFromList(SearchSource::REMOTE, 0);
                match.eunitId = CurrObj::get(ObjData::BASE_TYPE);
                match.eunitCount = DUC::remoteList::size();
            }
            end_if();
            
            // auto patrol
            
            begin_if(match.status == Status::READY);
            {
                // DUC::localList::targetRemoteObjects(TargetActionB::PATROL);
                DUC::localList::targetPoint(DUC::remoteList::medianPos(), TargetActionA::PATROL);
                match.status = Status::RUNNING; 
            }
            end_if();
            
            // get final data
            
            begin_if(PlayerID::SELF == (VarPtr) PlayerID::PLAYER_2 && match.status == Status::RUNNING && (DUC::localList::empty() || DUC::remoteList::empty() || timeSec > 2*60+30));
            {
                match.status = Status::COMPLETED;
                match.hpFinal = DUC::localList::getSum(ObjData::HITPOINTS);
                match.ehpFinal = DUC::remoteList::getSum(ObjData::HITPOINTS);
                chat("match completed: ", j, PlayerID::ALL);
            }
            end_if();

            // auto re-target if not attacking anything
            
            begin_if(timeSec > 30 && skips(5) && DUC::remoteList::notEmpty() && DUC::localList::notEmpty());
            {
                DUC::localList::remove(ObjData::PATROLLING, CompareOp::EQUAL, true);
                DUC::localList::remove(ObjData::TASKS_COUNT, CompareOp::GREATER_THAN, 0);
                DUC::localList::remove(ObjData::ACTION, CompareOp::EQUAL, ActionID::ATTACK);
                DUC::localList::remove(ObjData::ACTION, CompareOp::EQUAL, ActionID::MOVE);
                DUC::localList::targetRemoteObjects();
                // begin_if(DUC::localList::notEmpty());
                // chat("re-target", j, PlayerID::ALL);
                // end_if();
            }
            end_if();

            // set match data
            matchData.set(j*sizeMatch+0, match.unitId);
            matchData.set(j*sizeMatch+1, match.hpInitial);
            matchData.set(j*sizeMatch+2, match.hpFinal);
            matchData.set(j*sizeMatch+3, match.unitCount);
            matchData.set(j*sizeMatch+4, match.eunitId);
            matchData.set(j*sizeMatch+5, match.ehpInitial);
            matchData.set(j*sizeMatch+6, match.ehpFinal);
            matchData.set(j*sizeMatch+7, match.eunitCount);
            matchData.set(j*sizeMatch+8, match.status);
        }
        end_for();

        // write data to file via xs script
        begin_if(allDone && PlayerID::SELF == (VarPtr) PlayerID::PLAYER_2);
        {
            chat("dumping data to file", PlayerID::ALL);
            callXSFunction("dumpData");
            Engine::add_action({ ActionNumber::DISABLE_SELF, {} });
        }
        end_if();

        
        // write xs script

		string xsLocation = "E:/SteamLibrary/steamapps/common/AoE2DE/resources/_common/xs";
		string xsName = "Dump.xs";
        int startIndex = Engine::lookupVarIdint(matchData.getAOCenum(false).enumValue);
        int stopIndex = startIndex + max_rows*max_cols*sizeMatch - 1;

        std::ofstream out(xsLocation+"/"+xsName);

        out << 
        "void dumpData()\n"
        "{\n"
        "    xsChatData(\"xs script is running\", 0);\n"
        "    xsSetContextPlayer(2);\n"
        "    xsCreateFile(false);\n"
        "    int tmp = 0;\n";

        for (int i=startIndex; i<=stopIndex; i++)
        {
            out << "    tmp = xsGetGoal(" << i << "); xsWriteInt(tmp);\n";
        }

        out <<
        "    xsSetContextPlayer(-1);\n"
        "    xsCloseFile();\n"
        "}\n"
        "\nvoid main(){ }\n";

        out.close();

    }
};
