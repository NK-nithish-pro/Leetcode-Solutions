
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        l=0
        r=len(height)-1
        while l<r:
            width = r-l
            minimum=min([height[l],height[r]])
            a=width*minimum

            if a > area:
                area = a
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return area