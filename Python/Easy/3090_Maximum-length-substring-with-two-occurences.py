class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        r=0
        freq={s[l]:1}
        max_length=1
        
        r+=1
        while r<len(s):
            if s[r] not in freq:
                freq[s[r]]=1
            else:
                freq[s[r]]+=1
            

            if freq[s[r]]<=2:
                if r-l+1>max_length:
                    max_length=r-l+1
                
                
            else:
                while freq[s[r]]>2:
                    freq[s[l]]-=1
                
                    l+=1
                

                
            r+=1
                
        
        return max_length