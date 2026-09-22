from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            nm = nums[m]
            nr = nums[r]
            
            if nm == target:
                return m
            elif nm < nr:
                # 右半段有序
                if target > nr:
                    r = m - 1
                else:  # target <= nr 的情况
                    if target > nm:
                        l = m + 1
                    else:
                        r = m - 1
            else:  # nm >= nr，包含 nm > nr 以及区间收缩到 m == r 的情况
                # 左半段有序
                if target <= nr:  # 修正：加等号，包含 target == nr 在右半段的情况
                    l = m + 1
                else:  # target > nr 的情况
                    if target < nm:
                        r = m - 1
                    else:
                        l = m + 1
                        
        return -1