class MinStack:

    def __init__(self):
        self.prev=[]
        self.Stack=[]
        self.minimum=0
        #self.count={}

    def push(self, value: int) -> None:
        #if value not in self.count:
            #self.count[value]=1
        #else:
           # self.count[value]+=1
        if len(self.Stack)!=0:
            if self.minimum>=value:
                self.prev.append(value)
                self.minimum=value
            
            self.Stack.append(value)
        else:
            self.minimum=value
            self.prev.append(value)
            self.Stack.append(self.minimum)

    def pop(self) -> None:
        #self.count[self.Stack[-1]]-=1
        if self.Stack[-1]==self.minimum:
            
            #if self.count[self.minimum]==0:
                    self.prev.pop()
                    if self.prev!=[]:
                        self.minimum=self.prev[-1]
        self.Stack.pop()
        
        '''if len(self.Stack)>0:
            if len(self.Stack)==1:
                self.minimum=self.Stack[-1]
            else:
                r=len(self.Stack)-1
                self.small=self.Stack[0]
                while r>=0:
                    if self.Stack[r]<self.small:
                        self.small=self.Stack[r]
                        
                    r-=1
                
                if self.small==self.minimum:
                    pass
                else:
                    if self.small!=0:
                        self.minimum=self.small'''
            
    def top(self) -> int:
        return self.Stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()