class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        if s=="":
            return 0
        window={s[l]:l}
        max_length=r-l+1
        r+=1

        
        

        while r<len(s):

            if s[r] in window:
                if window[s[r]]>=l:
                    l=window[s[r]]+1
                window[s[r]]=r
                
                r+=1
            else:
                window[s[r]]=r
                
                r+=1
            if (r-1)-l+1>max_length:
                max_length=(r-1)-l+1
                
                
            
            
            
        return max_length


            


        
        