
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        answer = -1
        position = []

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                answer = mid
                r = mid - 1
        
        if answer==-1:
            return [-1,-1]
                
        position.append(answer)
        l = answer + 1
        r = len(nums) - 1

        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                answer=mid
                l=mid+1

                
        position.append(answer)

        return position
        



