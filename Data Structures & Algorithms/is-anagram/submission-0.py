class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        for n in s:
            a[n] = a.get(n,0) +1
        
        for n in t:
            if n in a and a[n]!= 0:
                a[n] -=1
            else:
                return False
        
        return True
            
        