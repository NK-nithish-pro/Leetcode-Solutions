
#Leetcode Problem 1833
#Difficulty - Medium
#Solved on 21.06.26

#Same idea but different implementations

#1) Tracks the total money and checks whether it is exceeding the coins
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        maxIce=0
        c=sorted(costs)
        total=0
        for i in c:
            total+=i
            if total<=coins:
                maxIce+=1
            else:
                break    
        return maxIce

#Alternate solution - tracks how much total money is spent and checks whether coins is available enough each time

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxIce=0
        c=sorted(costs)
        total=coins
        for i in c:
            total-=i
            if total>=0:
                maxIce+=1

        return maxIce
        
