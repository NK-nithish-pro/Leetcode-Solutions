#two pointer approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l<r:
            rem = s[l]
            s[l] = s[r]
            s[r] = rem
            r-=1
            l+=1

#Direct built-in method
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()