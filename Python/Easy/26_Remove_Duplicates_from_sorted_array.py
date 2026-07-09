
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        k=1
        while r<len(nums):
            if nums[l]==nums[r]:
                r+=1
                continue
            else:
                rem=nums[l+1]
                nums[l+1]=nums[r]
                nums[r]=rem
                k+=1
                r+=1
                l+=1
        return k
        