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

    print(old)
    print(new)

    for stat in old:
        # RAWD41159
        #plt.scatter(i, old[stat], color="#1A85FF", marker="^", s=100)
        #plt.scatter(i, new[stat], color="#D41159", marker="*", s=100)

        # Percentage
        plt.bar(i, new[stat]/old[stat]*100, color="#D35FB7")
        #print(new[stat]/old[stat]*100)

        xNames.append(stat.upper())
        i+=1
    

### RAW 

    plt.xticks(range(len(xNames)), xNames)
    #plt.scatter(5.1, 630, color="#1A85FF", marker="^", s=100)
    #plt.annotate("2019 System", (5.1, 630), textcoords="offset points", xytext=(10,-4)) 

    #plt.scatter(5.1, 590, color="#D41159", marker="*", s=100)
    #plt.annotate("2020 System", (5.1, 590), textcoords="offset points", xytext=(10,-4))

    plt.title("Raw Metrics Relative Percentage Comparison")
    plt.ylabel("Relative Percentage Metrics 2020 vs 2019")
    plt.xlabel("Raw Metrics")

 
### Percentage
    #plt.xticks(range(len(xNames)), xNames)

    #plt.xlabel("Raw Metrics")     
    #plt.title("Raw Metrics Percentage Comparison")
    #plt.ylabel("Percentage Metrics 2020 vs 2019") 

    plt.show()



def getJSON(filename):

    with open(filename) as json_file:
        data = json.load(json_file)

    return data

def plotHalstead(old, new):

    xNames= ["VOCABULARY", "LENGTH", "CALC_LENGTH", "VOLUME", "DIFFICULTY", "TIME", "BUGS"]
    
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
        # Raw#1A85FF
        #plt.scatter(i, halsteadTotalOld[i], color="#1A85FF", marker="^", s=100)
        #plt.scatter(i, halsteadTotalNew[i], color="#D41159", marker="*", s=100)

        # Percentage
        plt.bar(i, halsteadTotalNew[i]/halsteadTotalOld[i]*100, color="#D35FB7")
        
    plt.xticks(range(len(xNames)), xNames)

# RAW
    """
    plt.scatter(5.1, 2550, color="#1A85FF", marker="^", s=100)
    plt.annotate("2019 System", (5.1, 2550), textcoords="offset points", xytext=(10,-4)) 

    plt.scatter(5.1, 2350, color="#D41159",  marker="*", s=100)
    plt.annotate("2020 System", (5.1, 2350), textcoords="offset points", xytext=(10,-4))

    plt.xlabel("Halstead Metrics")     
    plt.ylabel("Metrics Size") 
    plt.title("Halstead Metrics Detailed Comparison")
    """
#Percentage
 
    plt.xlabel("Halstead Metrics")     
    plt.ylabel("Relative Percentage Metrics 2020 vs 2019") 
    plt.title("Halstead Metrics Relative Percentage Comparison")


    plt.show()

def plotCC_MI(oldMI, newMI):
    # Since CC gives us averaging over all the files, we'll use that

    xNames = ["CC", "MI"]

    oldCC = 4.50
    newCC = 3.06

    oldTotal = 0
    newTotal = 0

    for filename in oldMI:
        oldTotal += oldMI[filename]["mi"]
    for filename in newMI:
        newTotal += newMI[filename]["mi"]

    plt.xticks(range(len(xNames)), xNames)

    #plt.bar(0, 100, color="#1A85FF")
    #plt.bar(0, newCC/oldCC*100, color="#D35FB7")
    plt.scatter(0, oldCC, color="#1A85FF", s=100, marker="^")
    plt.scatter(0, newCC, color="#D41159", s=100, marker="*")

    newAverage= newTotal/len(newMI)
    oldAverage= oldTotal/len(oldMI)

    #plt.bar(1, newAverage/oldAverage*100, color="#D35FB7")
    #plt.bar(1, 100, color="#1A85FF")
    plt.scatter(1, oldAverage, color="#1A85FF", s=100, marker="^")
    plt.scatter(1, newAverage, color="#D41159", s=100, marker="*")

    plt.scatter(0, 80, color="#1A85FF", marker="^", s=100)
    plt.annotate("2019 System", (0, 80), textcoords="offset points", xytext=(10,-4)) 

    plt.scatter(0, 75, color="#D41159", marker="*", s=100)
    plt.annotate("2020 System", (0, 75), textcoords="offset points", xytext=(10,-4))

    plt.ylabel("Relative Percentage Metrics 2020 vs 2019")
    plt.xlabel("Cyclomatic Complexity and Maintainability Index")
    plt.title("CC and MI Relative Percentage Comparison")
    plt.show()


if __name__=="__main__":
    plotRaw(getJSON("std_fsai/raw.txt"), getJSON("ros_fsai/raw.txt"))
    