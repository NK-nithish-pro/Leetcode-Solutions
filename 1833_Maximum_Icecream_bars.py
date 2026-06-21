
#Leetcode Problem 1833
#Difficulty - Medium
#Solved on 21.06.26

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

#Alternate solution
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
        