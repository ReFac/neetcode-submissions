class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = Counter(t)
        left = 0
        check = 0
        smallest = 999999
        result = ''
        for i,x in enumerate(s):
            if x in count:
                count[x] -= 1
                if count[x] == 0:
                    check +=1
            while check == len(count):
                if (i-left+1) < smallest:
                    smallest = (i-left+1)
                    result = s[left:i+1:1]
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] == 1:
                        check -=1
                left +=1
        return result
                
        
