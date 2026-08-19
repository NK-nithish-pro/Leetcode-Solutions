class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        sub_freq={}
        
        
        
        while r<len(nums):
            if nums[r] not in sub_freq:
                    sub_freq[nums[r]]=1
            else:
                if l>0:#Has l moved forward since my first window" Has the first window already been completed....It mainly checks whether first window is over...
                    sub_freq[nums[r]]+=1
                    
                
                    
                
            
            
            if r-l+1 == k:
                l+=1
                r=l
                
                if r+(k-1)>len(nums)-1:
                    break
            else:
                r+=1
        
        largest=[k for k,v in sub_freq.items() if v==1]
        if largest==[]:
            return -1
        else:
            return max(largest)