class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def add(point):
            dist = math.sqrt((point[0] - 0)^2 + (point[1] - 0)^2)
            if len(heap)<k:
                heapq.heappush(heap, (-dist,point))
            else:
                if heap[0][0] > dist:
                    heapq.heapreplace(heap,(-dist,point))
        
        for point in points:
            add(point)
        res =[]
        for dist,point in heap:
            res.append(point)
        return res
            


        