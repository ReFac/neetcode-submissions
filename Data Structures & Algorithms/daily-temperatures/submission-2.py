class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t1 = temperatures[::-1]
        rl = []
        result = []
        for t in t1:
            if not rl:
                rl.append((t,1))
                result.append(0)
            else:
                count = 1
                while rl:
                    a = rl[-1]
                    if a[0] > t:
                        rl.append((t,count))
                        result.append(count)
                        break
                    else:
                        rl.pop()
                        count += a[1]
                if not rl:
                    rl.append((t,1))
                    result.append(0)
        return result[::-1]
            
                        


