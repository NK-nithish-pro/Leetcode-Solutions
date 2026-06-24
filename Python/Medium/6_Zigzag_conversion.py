class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag=""
        rows=[""]*numRows
        currentrow=0
        direction=1
        if numRows==1:
            return s
        else:
            for i in s:
            
                rows[currentrow]+=i
                if currentrow==numRows-1:
                    direction=-1
                if currentrow==0:
                    direction=1
        
                currentrow+=direction

            for j in rows:
                zigzag+=j
        
            return zigzag
        