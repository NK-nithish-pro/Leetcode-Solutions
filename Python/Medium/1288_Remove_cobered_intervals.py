
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        copy=sorted(intervals)
        intervals.sort()


        for i in intervals:
            for j in intervals:
                if i == j :
                    continue
            
                if i[0]>=j[0] and i[1]<=j[1]:
                    copy.remove(i)
                    break
        return len(copy)