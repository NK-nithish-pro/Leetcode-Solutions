
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=0
        a=0
        l=0
        o=0
        n=0
       
        
        copy="balloon"
        for i in text:
            if i == "b":
                b+=1
            if i=="a":
                a+=1
            if i=="l":
               l+=1
            if i=="o":
               o+=1
            if i=="n":
                n+=1
        count=[b,a,l//2,o//2,n]    
        return min(count)   