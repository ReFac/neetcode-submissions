class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            nm = nums[m]
            nr = nums[r]
            if nm == target:
                return m
            elif nm < nr:
                if target > nr:
                    r = m-1
                else:
                    if target > nm:
                        l = m+1
                    else:
                        r = m-1
            else:
                if target <= nr:
                    l = m+1
                else:
                    if target < nm:
                        r = m-1
                    else:
                        l = m+1
        return -1
                    


        