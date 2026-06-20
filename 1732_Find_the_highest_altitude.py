
def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        point=0
        n=len(gain)

        for i in range(n):
            point+=gain[i]
            altitudes.append(point)

        return max(altitudes)   