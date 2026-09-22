class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        indexs = []
        heights = [0] + heights + [0]
        largest = 0

        for i, x in enumerate(heights):
            while indexs and heights[indexs[-1]] > x:
                y = indexs.pop()
                yh = heights[y]
                area = yh*(i - indexs[-1] - 1)
                largest = max(area,largest)
            
            indexs.append(i)

        return largest
        