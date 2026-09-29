class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        

    def addNum(self, num: int) -> None:
        if not self.heap1 and not self.heap2:
            heapq.heappush(self.heap1,num)
        elif not self.heap2:
            if self.heap1[0] >= num:
                heapq.heappush(self.heap2,-num)
            else:
                x = self.heap1[0]
                heapq.heapreplace(self.heap1,num)
                heapq.heappush(self.heap2,-x)
        else:
            if len(self.heap1) > len(self.heap2):
                x = self.heap1[0]
                if x >= num:
                    heapq.heappush(self.heap2,-num)
                else:
                    heapq.heapreplace(self.heap1,num)
                    heapq.heappush(self.heap2,-x)
            else:
                x = -self.heap2[0]
                if x <= num:
                    heapq.heappush(self.heap1,num)
                else:
                    heapq.heapreplace(self.heap2,-num)
                    heapq.heappush(self.heap2,x)

                

    def findMedian(self) -> float:
        if len(self.heap1) > len(self.heap2):
            return self.heap1[0]
        else:
            return (self.heap1[0]-self.heap2[0])/2
        
        