
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)
        middle=int((n+1)/2-1)
        if nums.count(nums[middle])>1:
            return False
        else:
            return True
