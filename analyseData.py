import json
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

def plotRaw(old, new):
    
    totalOld = {}
    for filename in old:
        for stat in old[filename]:
            if stat not in totalOld:
                totalOld[stat] = old[filename][stat]
            else:
                totalOld[stat] += old[filename][stat]

    totalNew = {}
    for filename in new:
        for stat in new[filename]:
            if stat not in totalNew:
                totalNew[stat] = new[filename][stat]
            else:
                totalNew[stat] += new[filename][stat]

    old = totalOld
    new = totalNew
    xNames = []
    i=0
    for stat in old:
        print(old[stat])
        plt.scatter(i, old[stat], color="r")
        plt.scatter(i, new[stat], color="g")
        xNames.append(stat.upper())
        i+=1

    plt.xticks(range(len(xNames)*3), xNames)

    plt.scatter(5.5, 630, color="r", label="Ros Integration", marker="s")
    plt.annotate("2019 System", (5.5, 630), textcoords="offset points", xytext=(10,-4)) 

    plt.scatter(5.5, 590, color="g", label="Ros Integration", marker="s")
    plt.annotate("ROS System", (5.5, 590), textcoords="offset points", xytext=(15,-4))

    plt.title("Raw Metrics Detailed Comparison")
                          
    plt.show()

def getJSON(filename):

    with open(filename) as json_file:
        data = json.load(json_file)

    return data

def plotHalstead(old, new):

    xNames= ["VOCABULARY", "LENGTH", "CALCULATED_LENGTH", "VOLUME", "DIFFICULTY", "TIME", "BUGS"]
    
    halsteadTotalOld = [0,0,0,0,0,0,0]
    halsteadTotalNew = [0,0,0,0,0,0,0]

    for filename in old:
        i=0
        passed=True
        for stat in old[filename]["total"][4:]:
            if i==5 and passed:
                passed=False
                continue
            halsteadTotalOld[i]+=stat
            i+=1

    for filename in new:
        i=0
        passed=True
        for stat in new[filename]["total"][4:]:
            if i==5 and passed:
                passed=False
                continue
            halsteadTotalNew[i]+=stat
            i+=1

    for i in range(len(halsteadTotalNew)):
        plt.scatter(i, halsteadTotalNew[i]/halsteadTotalOld[i]*100, color="b")
        
    plt.xticks(range(len(xNames)), xNames)

    plt.scatter(4.5, 100, color="b", label="Ros Integration", marker="s")
    plt.annotate("Ros System vs 2019 System", (4.5, 100), textcoords="offset points", xytext=(10,-4)) 

    # plt.scatter(5.5, 2350, color="g", label="Ros Integration", marker="s")
    # plt.annotate("ROS System", (5.5, 2350), textcoords="offset points", xytext=(15,-4))

    plt.title("Halstead Percentage Comparison")
    plt.show()


if __name__=="__main__":
    plotHalstead(getJSON("std_fsai/hal.txt"), getJSON("ros_fsai/hal.txt"))
    