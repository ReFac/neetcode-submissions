class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = -1
        ma = max(piles)
        nlen = len(piles)

        if h == nlen :
            return ma
        elif h < nlen:
            return -1
        
        left = 1
        right = ma
        while left <= right:
            m = left + (right - left)//2
            npiles = (math.ceil(i/m) for i in piles)
            t = sum(i for i in npiles)
            if t <= h:
                right = m-1
                result = m
            elif t > h:
                left = m+1

        return result

        