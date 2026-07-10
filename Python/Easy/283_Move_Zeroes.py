
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while r<len(nums):
            if nums[r]==0:
                r+=1
                continue
            else:
                rem=nums[l]
                nums[l]=nums[r]
                nums[r]=rem
                r+=1
                l+=1
            