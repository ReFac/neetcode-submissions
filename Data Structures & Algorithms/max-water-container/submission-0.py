class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <=1 :
            return 0
        left = 0
        right = len(heights)-1
        water = (right-left)*min(heights[left], heights[right])
        result = water
        while left < right:
            if heights[left] <= heights[right]:
                while left < right:
                    left +=1
                    new = (right-left)*min(heights[left], heights[right])
                    if new >= water:
                        result = max(new,result)
                        break

            if heights[left] >= heights[right]:
                while left < right:
                    right -=1
                    new = (right-left)*min(heights[left], heights[right])
                    if new >= water:
                        result = max(new,result)
                        break

        return result




        