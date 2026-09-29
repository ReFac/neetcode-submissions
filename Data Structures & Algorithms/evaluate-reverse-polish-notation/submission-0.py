class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n < 3:
            return 0
        i = 2
        result = int(tokens[0])
        while i < n:
            if tokens[i] == "+":
                result = result + int(tokens[i-1])
            elif tokens[i] == "*":
                result = result * int(tokens[i-1])
            elif tokens[i] == "-":
                result = result - int(tokens[i-1])
            i = i+2
        
        return result