# LeetCode 1732 - Find the Highest Altitude
# Difficulty: Easy
# Solved: 19-06-2026

class Solution:
def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        point=0
        n=len(gain)

        for i in range(n):
            point+=gain[i]
            altitudes.append(point)

        return max(altitudes)   
