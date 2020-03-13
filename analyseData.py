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
        #plt.annotate(stat.upper(), (i, old[stat]), textcoords="offset points", xytext=(12,0))      

        #plt.plot((i-0.5, i-0.5), (new[stat], old[stat]), color="b")
        #plt.plot((i+0.6, i+0.6), (new[stat], old[stat]), color="b")
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

def createMI(old, new):
    old = getJSON(old+"mi.txt")
    new = getJSON(new+"mi.txt")
    
    totalMI = 0
    counter = 0

    allFiles = {}

    for filename in old:
        if filename not in allFiles:
            allFiles[filename] = [ ("old", old[filename]["mi"] ) ]
        else:
            allFiles[filename].append( ("old", old[filename]["mi"]) )
    
    for filename in new:
        if filename not in allFiles:
            allFiles[filename] = [ ("new", new[filename]["mi"]) ]
        else:
            allFiles[filename].append( ("new", new[filename]["mi"] ))

    xNames = []
    yValuesOld = []; oldMITotal = 0; oldMICounter = 0
    yValuesNew = []; newMITotal = 0; newMICounter = 0

    for filename in allFiles:
        xNames.append(filename)
        addOld = True; addNew = True
        for element in allFiles[filename]:
            if element[0] == "old":
                yValuesOld.append(element[1])
                oldMITotal += element[1]
                oldMICounter +=1
                addOld = False
            elif element[0] == "new":
                newMITotal += element[1]
                newMICounter +=1
                yValuesNew.append(element[1])
                addNew = False

        if addOld:
            yValuesOld.append(100)
        if addNew:
            yValuesNew.append(100)
        
    print("Filenames: ", xNames)
    print("Old:", yValuesOld)
    print("New: ", yValuesNew)

    
    xValues = range(len(xNames))


    plt.xticks(xValues, xNames)
    plt.scatter(xValues, yValuesOld, color="r")
    plt.scatter(xValues, yValuesNew, color="g")

    plt.plot(xValues, [oldMITotal/oldMICounter]*len(xValues), "r", label="2019 System")
    plt.plot(xValues, [newMITotal/newMICounter]*len(xValues), "g", label="ROS System")

    plt.xlabel("Filenames")
    plt.ylabel("Maintainability Index")

    plt.show()


if __name__=="__main__":
    plotRaw(getJSON("std_fsai/raw.txt"), getJSON("ros_fsai/raw.txt"))
    