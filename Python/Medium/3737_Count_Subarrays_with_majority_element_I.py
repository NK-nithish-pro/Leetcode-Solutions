#optimised Solution
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(len(nums)):
            sub=[nums[i]]
            length=1
            target_count=0
            if target in sub:
                target_count=1
                if target_count>length/2:
                    count+=1
            for j in range(i+1,len(nums)):
                sub.append(nums[j])
                length+=1
                if nums[j]==target:
                    target_count+=1
                if target_count>length/2:
                    count+=1

        return count   
            
            

        
        
        
        








"""
subarrays=[]
nums=[1,2,3]
for i in range(len(nums)):
            n=1
            while n<len(nums)+1:
                array=[]
                for j in range(i,n):
                    array.append(nums[j])
                    if j == n-1:
                        subarrays.append(array)
                
                n+=1

print(subarrays)