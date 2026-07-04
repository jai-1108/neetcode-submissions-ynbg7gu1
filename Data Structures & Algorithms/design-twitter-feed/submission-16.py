class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweet = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer -= 1
        self.tweet[userId].append([self.timer,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower[userId].add(userId)
        res = []
        heap = []
        for followee in self.follower[userId]:
            if followee in self.tweet:
                index = len(self.tweet[followee]) - 1
                time, tweetid = self.tweet[followee][index]
                heapq.heappush(heap, [time, tweetid, followee, index-1])
        
        while heap and len(res) < 10:
            time, tweetid, followeeId, index = heapq.heappop(heap)
            res.append(tweetid)
            if index >= 0:
                time, tweetid = self.tweet[followeeId][index]
                heapq.heappush(heap,[time, tweetid, followeeId, index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
