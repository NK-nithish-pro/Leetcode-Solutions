#two pointer approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=len(s)-1
        l=0
        
        while l<r:
            if s[l].isalnum()==False:
                l+=1
                continue
            elif s[r].isalnum()==False:
                r-=1
                continue
            else:
                if s[l].lower()!=s[r].lower():
                
                    return False
            l+=1
            r-=1
        return True

#Bruteforce
class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy=""
        for i in s:
            if i.isalnum():
                copy+=i.lower()
        if copy=="":
            return True
        
        if copy==copy[::-1]:
            return True
        else:
            return False