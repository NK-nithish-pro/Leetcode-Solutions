
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid)==False:
                l=mid+1
            else:
                r=mid-1
        return l