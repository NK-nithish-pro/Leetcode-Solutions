#Arithmetic approach
class Solution:
    def reverse(self, x: int) -> int:
        y=abs(x)
        reverse=0
        while y>0:
            digit=y%10
            reverse=reverse*10+digit
            y//=10
        if x<0:
            reverse=reverse*-1
        if reverse<(-(2**31)) or reverse>(2**31-1):
            return 0
        else:
            return reverse




#String approach
class Solution:
    def reverse(self, x: int) -> int:
        reverse_string=""
        string = str(x)
        if "-" == string[0]:
            reverse_string+="-"
            string=string[1:]
        reverse_string+=string[::-1]
        reverse_num=int(reverse_string)
        if reverse_num<(-(2**31)) or reverse_num>((2**31)-1):
            return 0
        else:
            return reverse_num


