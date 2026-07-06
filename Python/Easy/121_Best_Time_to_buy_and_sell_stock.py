#optimised solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        
        best_buy=prices[0]
        for i in range(1,len(prices)):
            profit = prices[i] - best_buy
            if profit>max_profit:
                max_profit=profit
            if prices[i]<best_buy:
                best_buy=prices[i]

        return max_profit

#Bruteforce approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        for i in range(len(prices)):
            profit=0
            
            for j in range(i+1,len(prices)):
                if prices[i]>prices[j]:
                    continue
                else:
                    profit = prices[j]-prices[i]
                
                if max_profit<profit:
                    max_profit=profit
        return max_profit
        