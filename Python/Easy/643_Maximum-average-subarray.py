
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k-1
        
        max_sum=sum(nums[l:r+1])
        Sum=max_sum
        max_avg=max_sum/k

        

        l+=1
        r+=1
        
        while r<=len(nums)-1:
            
                s=Sum-nums[l-1]+nums[r]
                Sum=s
                

            
                if Sum>max_sum:
                    max_sum=s
                    max_avg = max_sum/k
                
                l+=1
                r+=1            
            

        return max_avg