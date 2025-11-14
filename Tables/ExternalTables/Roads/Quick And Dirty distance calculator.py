import math

maxTime = 4095

coords = [
    [312,216], #Node 1
    [312,240], #Road point 1
    [264,240], #Road point 2
    #[x,y], #Road point 3
    #[x,y], #Road point 4
    [264,232] #Node 2
]
distances = []

totalDistance = 0
for i in range(len(coords)-1):
    dist = math.dist(coords[i],coords[i+1])
    totalDistance += dist
    distances.append(dist)
    #if i != (len(coords)-2):
    #    print(dist)

print("---")

accumulatedDist = 0
for i in range(len(distances)-1):
    dist = distances[i]
    accumulatedDist += dist
    print("Road point #"+str(i+1)+" - "+str(round(accumulatedDist/totalDistance*maxTime)))