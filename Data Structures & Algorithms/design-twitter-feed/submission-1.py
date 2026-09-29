class Twitter:

    def __init__(self):
        self.lib ={}
        self.follows ={}
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.lib:
            heap = self.lib[userId]
            heapq.heappush(heap,(self.timeStamp,tweetId))
            self.timeStamp -=1
        else:
            self.lib[userId] = []
            self.follows[userId] = []
            self.follows[userId].append(userId)
            heap = self.lib[userId]
            heapq.heappush(heap,(self.timeStamp,tweetId))
            self.timeStamp -=1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.lib:
            res = []
            ret = []
            heaps = []
            lst = self.follows[userId]
            size = 0
            for x in lst:
                heaps.append(self.lib[x])
                size += len(self.lib[x])
            size = min(size,10)
            for i in range(size):
                time = 1
                pop = -1
                for i,x in enumerate(heaps):
                    if x:
                        t = x[0][0]
                        if t < time:
                            pop = i
                            time = t
                if pop == -1:
                    break
                (times,vals) = heapq.heappop(heaps[pop])
                res.append((times,vals,pop))
            for time,val,pop in res:
                heapq.heappush(heaps[pop],(time,val))
                ret.append(val)
            return ret
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            fo = self.follows[followerId]
            fo.append(followeeId)
        else:
            self.lib[followerId] = []
            self.follows[followerId] = []
            self.follows[followerId].append(followerId)
            self.follows[followerId].append(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            pass
        elif followerId not in self.follows:
            pass
        else:
            fo = self.follows[followerId]
            try:
                fo.remove(followeeId)
            except ValueError:
                pass 
        
