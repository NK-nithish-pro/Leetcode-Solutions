
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=0
        k=0
        while r<len(nums):
            if nums[r]==val:
                r+=1
                continue
            else:
                nums[l]=nums[r]
                k+=1
                l+=1
                r+=1
        return k