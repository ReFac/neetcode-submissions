class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res= []
        dic = {
            "1": "",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def helper(i,sub):
            if i == len(digits):
                res.append(sub)
                return
            cur = digits[i]
            for cr in dic[cur]:
                helper(i+1,sub+cr)
        
        
        helper(0,"")
        return res
            
        