import json
import matplotlib.pyplot as plt

def plotRaw(old, new):
    
    for filename in old:
        if filename == "autocross.py":
            i=0 
            for stat in old[filename]:
                print(old[filename][stat])
                plt.scatter(i, old[filename][stat], color="r")
                plt.scatter(i, new[filename][stat], color="g")
                plt.annotate(stat, (i, old[filename][stat]), textcoords="offset points", xytext=(12,0))      

                plt.plot((i-0.5, i-0.5), (new[filename][stat], old[filename][stat]), color="b")
                plt.plot((i+0.6, i+0.6), (new[filename][stat], old[filename][stat]), color="b")
                i+=5
    plt.scatter(30, 140, color="r", label="Ros Integration")
    plt.annotate("2019 System", (30, 140), textcoords="offset points", xytext=(12,0)) 

    plt.scatter(30, 120, color="g", label="Ros Integration")
    plt.annotate("Ros Integration", (30, 120), textcoords="offset points", xytext=(12,0))

    plt.scatter(50, 120, color="g")
                          
    plt.show()
    input()

def analyseRaw(filename):

    with open(filename) as json_file:
        data = json.load(json_file)

    for key in data:
        print(key, data[key])

    return data



if __name__=="__main__":
    old = analyseRaw("std_fsai/raw.txt")
    print("VS")
    new = analyseRaw("ros_fsai/raw.txt")

    plotRaw(old, new)
    