class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = Counter(t)
        left = 0
        check = 0
        l_c = len(count)
        smallest = float("inf")
        start = -1
        for i,x in enumerate(s):
            if x in count:
                count[x] -= 1
                if count[x] == 0:
                    check +=1
            while check == l_c:
                if (i-left+1) < smallest:
                    smallest = (i-left+1)
                    start = left
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] == 1:
                        check -=1
                left +=1
        return s[start:start+smallest] if start!= -1 else "" 
                
        
