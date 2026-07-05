class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweet = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer -= 1
        self.tweet[userId].append([self.timer, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follower[userId].add(userId)
        followees = self.follower[userId]
        maxHeap = []
        res = []
        for followee in followees:
            if followee in self.tweet.keys():
                index = len(self.tweet[followee]) - 1
                time, tweetid = self.tweet[followee][index]
                heapq.heappush(maxHeap, [time, tweetid, followee, index - 1])
        while maxHeap and len(res) < 10:
            time, tweetid, followee, index = heapq.heappop(maxHeap)
            res.append(tweetid)
            if index >= 0:
                time, tweetid = self.tweet[followee][index]
                heapq.heappush(maxHeap, [time, tweetid, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId] and followerId != followeeId:
            self.follower[followerId].remove(followeeId)

