class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        sub = []
        n = len(s)

        def isPalindrome(l,r):
            while (l<r):
                if s[l] != s[r]:
                    return False
                    break
                l += 1
                r -= 1
            return True

        def helper(i):
            if i == n:
                result.append(sub.copy())
                return

            for end in range(i,n):
                if isPalindrome(i,end):
                    sub.append(s[i:end+1])
                    helper(end+1)
                    sub.pop()
        helper(0)

        return result


        
        