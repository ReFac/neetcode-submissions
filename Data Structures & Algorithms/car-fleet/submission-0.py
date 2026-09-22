class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        for i in range(len(position)-1,-1,-1):
            ps.append((target - position[i],speed[i]))

        ps.sort()
        
        count = 0
        currTime = -float("inf")

        for p,s in ps:
            if currTime < p/s:
                count +=1
                currTime = p/s
        return count
        