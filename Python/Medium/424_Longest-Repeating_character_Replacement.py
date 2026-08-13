
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l=0
        r=0
        
        max_length=1
        freq={s[l]:1}
        
        max_freq=freq[s[r]]
        
        count=0
        r+=1
        
        while r<len(s):
            
            if s[r] not in freq:
                freq[s[r]]=1
            else:
                freq[s[r]]+=1
            max_freq=max(max_freq,freq[s[r]])
            if (r-l+1)-max_freq<=k:
                if r-l+1>max_length:
                    max_length=r-l+1 
                
                
            else:
                
                freq[s[l]]-=1
                l+=1
                
            r+=1

            
                
            
            

        return max_length 