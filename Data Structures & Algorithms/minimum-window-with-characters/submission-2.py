class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count = Counter(t)
        left = 0
        check = 0
        smallest = float("inf")
        result = (-1,-1)
        for i,x in enumerate(s):
            if x in count:
                count[x] -= 1
                if count[x] == 0:
                    check +=1
            while check == len(count):
                if (i-left+1) < smallest:
                    smallest = (i-left+1)
                    result = (left,i+1)
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] == 1:
                        check -=1
                left +=1
        return s[result[0]:result[1]] if result[0]!= -1 else "" 
                
        
