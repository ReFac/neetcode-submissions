class Solution:

    def encode(self, strs: List[str]) -> str:
        text = []
        for s in strs:
            text.append(f"{len(s)}#{s}")
        return "".join(text)

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0 
        while(i < len(s)):
            j = i+1
            while s[j]!="#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1:j+1+length])
            i = j+1+length
        return strs


        

