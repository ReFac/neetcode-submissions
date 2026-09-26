class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxCount = max(count.values())
        maxFrq = sum(1 for i in count.values() if i == maxCount)
        return max((maxCount-1)*(n+1)+maxFrq,len(tasks))