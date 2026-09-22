class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        left = 0
        lc = len(count)
        c = 0
        l =float('inf')
        mleft = 0
        for i, x in enumerate(s):
            if x in count:
                count[x] -=1
                if count[x] == 0:
                    c +=1
            while c == lc:
                if (i-left+1) < l:
                    l = (i-left+1)
                    mleft = left
                if s[left] in count:
                    count[s[left]] +=1
                    if count[s[left]] == 1:
                        c -=1
                left +=1

        return s[mleft:mleft+l] if l <float('inf') else ""
                    

            
        