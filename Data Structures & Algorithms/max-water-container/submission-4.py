class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <=1 :
            return 0
        left = 0
        right = len(heights)-1
        result = 0
        while left < right:
            water = (right-left)*min(heights[left], heights[right])
            result = max(result,water)
            if heights[left] <= heights[right]:
                height = heights[left]
                while left < right and heights[left] <= height :
                    left +=1
            else:
                height = heights[right]
                while left < right and heights[right] <= height :
                    right -=1

        return result




        