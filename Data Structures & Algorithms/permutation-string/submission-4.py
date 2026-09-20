class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        lens2 = len(s2)
        if len(s1)>len(s2):
            return False

        setA = [0] *26
        setB = [0] *26

        for i in range(lens1):
            setA[ord(s1[i])-ord("a")] += 1
            setB[ord(s2[i])-ord("a")] += 1

        match = sum(1 for i in range(26) if setA[i] == setB[i])
        left = 0
        for i in range(lens1,lens2):
            if match == 26:
                return True
            index = ord(s2[i])-ord("a")
            setB[index] += 1
            if setB[index] == setA[index]:
                match +=1
            elif setB[index] == setA[index]+1:
                match -=1
            
            index = ord(s2[left])-ord("a")
            setB[index] -= 1
            if setB[index] == setA[index]:
                match +=1
            elif setB[index] == setA[index]-1:
                match -=1
            left += 1
        
        return match == 26



        
