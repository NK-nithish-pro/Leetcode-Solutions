import math as m
class Solution:
    
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        
        
        reach={}
       
        for i in range(0,len(drones)):
            md=(m.fabs(drones[i][0]-target[0]))+(m.fabs(drones[i][1]-target[1]))
            
                

            if md<=drones[i][2]:
                    if md in reach:
                        continue
                    else:
                        reach[md]=i

        if reach=={}:
            return -1
        else:
            return reach[min(reach)]