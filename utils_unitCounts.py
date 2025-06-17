
import utils_unit_data
from utils import *

unitData = utils_unit_data.getAllMatches()
utils_unit_data.loadResults(unitData)

def getCounts(c2, c3, a2, a3, u2, u3, costErr):

    # get unit data
    nameA2 = utils_unit_data.getMatchNameA(c2,a2)
    nameA3 = utils_unit_data.getMatchNameA(c3,a3)
    u2data = unitData[nameA2][u2]
    u3data = unitData[nameA3][u3]

    # get costs
    a2 = getAge(a2)
    a3 = getAge(a3)
    weight2 = resource_weights[a2]
    weight3 = resource_weights[a3]
    cost2 = weight2["F"]*u2data[3] + weight2["W"]*u2data[4] + weight2["S"]*u2data[5] + weight2["G"]*u2data[6]
    cost3 = weight3["F"]*u3data[3] + weight3["W"]*u3data[4] + weight3["S"]*u3data[5] + weight3["G"]*u3data[6]

    # get cost ratio
    costRatio = cost2/cost3

    # get avaliable count ratios
    allRatios = []
    for i in range(num_units-num_units_delta, num_units+num_units_delta+1):
        for j in range(1,i-1):

            c2 = j
            c3 = i-j
            count = i
            ratio = c2/c3
            delta = abs(i - num_units)
            delta2 = abs(ratio - costRatio)

            allRatios.append((c2,c3,count,ratio,delta,delta2))

    # delete identicle ratios

    allRatios = sorted(allRatios, key=lambda item: item[3]+item[4]/100000)

    allRatiosFinal = []
    for i in range(len(allRatios)):
        if i == 0 or abs(allRatios[i-1][3] - allRatios[i][3]) > 0.0001:
            allRatiosFinal.append(allRatios[i])
    allRatios = allRatiosFinal

    # find closest cost ratio
    allRatios = sorted(allRatios, key=lambda item: item[5])
    closestRatio = allRatios[0]

    # find closest ratio of the opposite sign
    delta2 = ratio - closestRatio[3]
    closestRatioOpp = closestRatio

    for r in allRatios:
        delta2_ = ratio - r[3]
        if delta2*delta2_ < 0:
            closestRatioOpp = r
            break

    return closestRatio
