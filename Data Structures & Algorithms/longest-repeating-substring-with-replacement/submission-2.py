class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count ={}
        highest = 0
        
        for right , ch in enumerate(s):
            count[ch] = count.get(ch,0) + 1
            highest = max(count[ch], highest)

            if (right - left + 1) > (highest + k):
                count[s[left]] -=1
                left +=1
        
        return len(s) - left