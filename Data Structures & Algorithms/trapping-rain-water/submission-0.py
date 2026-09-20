class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left = 0 
        right = len(height)-1
        result = 0
        while left < right:
            l_h = height[left]
            r_h = height[right]
            min_h = min(l_h,r_h)
            if l_h <= r_h:
                while left < right and height[left] <= min_h:
                    left +=1
                    t = min_h - height[left]
                    if t > 0:
                        result +=t
            else:
                while left < right and height[right] <= min_h:
                    right -=1
                    t = min_h - height[right]
                    if t > 0:
                        result +=t

            

        return result

        