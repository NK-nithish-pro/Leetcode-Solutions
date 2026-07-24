
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=k-1
        count=0
        for i in range(r+1):
            if s[i] in "aeiouAEIOU":
                count+=1
        
        max_count=count
        l+=1
        r+=1
        while r<len(s):
            
            if s[l-1] in "aeiouAEIOU":
                count-=1

            if s[r] in "aeiouAEIOU":
                
                count+=1
                if count>max_count:
                    max_count=count
                
                

                
            
            
            
            l+=1
            r+=1
        return max_count