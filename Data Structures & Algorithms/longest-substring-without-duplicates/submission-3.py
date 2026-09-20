class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lib = dict()
        left = right = 0
        max1 = 0
        while right< len(s):
            cur =s[right] 
            if cur in lib and lib[cur] >= left:
                left = lib[cur]+1

            lib[cur] = right
            right +=1
            max1 = max(max1,(right-left))
        return max1

            
            
        