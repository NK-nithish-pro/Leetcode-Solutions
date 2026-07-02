class Solution:
    def isValid(self, s: str) -> bool:
        o=["(","[","{"]
        c=[")","]","}"]
        stack=[]
        valid=False
        
        for i in s:
            
            if i in o:
                stack.append(i)
                
            elif stack==[] :
                return False
                break
            else:
                if c.index(i) == o.index(stack[-1]): 
                    valid = True
                    
                    stack.pop(-1)
                else:
                    return False
                    break
            
        if stack != []:
            valid = False   
        
        return valid
