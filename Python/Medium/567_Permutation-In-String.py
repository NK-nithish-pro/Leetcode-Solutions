class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        count={}
        check={}
        if len(s2)<len(s1):
            return False
        for i in s1:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        for i in range(r+1):
            if s2[i] in check:
                check[s2[i]]+=1
            else:
                check[s2[i]]=1#to count thee frequency of s1 characters
        while r<len(s2):
            if check==count:
                return True
            else:
                check[s2[l]]-=1
                if check[s2[l]] == 0:
                    del check[s2[l]]
                l+=1
                
                
                r+=1
                if r<len(s2):
                    if s2[r] in check:
                        check[s2[r]]+=1
                    else:
                        check[s2[r]]=1

        return False

        ###Variable sixe window-slightly complicated####
        '''while r<len(s2):
            if s2[r] not in count:
                r+=1
                continue
            else:
                check[s2[r]]=1
                l=r
                r+=1
                while r-l+1<=len(s1) and r<len(s2):
                    if s2[r] in count and s2[r] not in check:
                        check[s2[r]]=1
                        r+=1
                    elif s2[r] in count and check[s2[r]]>=count[s2[r]]:
                        while check[s2[r]]>=count[s2[r]]:
                             check[s2[l]]-=1
                             l+=1
                            
                        check[s2[r]]+=1
                        r+=1
                        
                    elif s2[r] in count and check[s2[r]]<count[s2[r]]:
                        check[s2[r]]+=1
                        r+=1
                        
                    else:
                        while l<r+1:
                            if s2[l] in check:
                                check[s2[l]]-=1
                            l+=1
                                
                        r=l
                        break
                if sum(check.values())==sum(count.values()):
                    return True

        
        
        return False'''


            

        