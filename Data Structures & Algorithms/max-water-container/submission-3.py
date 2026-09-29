class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <=1 :
            return 0
        left = 0
        right = len(heights)-1
        result = (right-left)*min(heights[left], heights[right])
        while left < right:
            if heights[left] <= heights[right]:
                while left < right:
                    left +=1
                    new = (right-left)*min(heights[left], heights[right])
                    if new >= result:
                        result = max(new,result)
                        break
            else:
                while left < right:
                    right -=1
                    new = (right-left)*min(heights[left], heights[right])
                    if new >= result:
                        result = max(new,result)
                        break

        return result




        