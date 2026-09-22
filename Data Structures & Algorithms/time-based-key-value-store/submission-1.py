class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        result = ''
        if key in self.storage:
            lenth = len(self.storage[key])
            left = 0
            right = lenth-1
            while left <= right:
                mid = left + (right-left)//2
                val = self.storage[key][mid][0]
                if val < timestamp:
                    left = mid +1
                    result = self.storage[key][mid][1]
                elif val > timestamp:
                    right = mid -1
                else:
                    return self.storage[key][mid][1]
        
        return result
                
                
        
        
