class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]* n
        pre = 1
        post = 1
        for i in range(n):
            ans[i] = pre
            pre = pre * nums[i]
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * post
            post = post * nums[i]

        return ans
            

        
        