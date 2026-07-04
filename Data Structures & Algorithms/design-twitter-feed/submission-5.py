class Twitter:

    def __init__(self):
        self.follower = defaultdict(set) #followerid mapped to a set of followeeids
        self.tweet = defaultdict(list) #userid mapped to tweetid and timestamp
        self.timer = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.tweet[userId].append([self.timer, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follower[userId] | {userId}
        all_tweets = []
        for followee in followees:
            for tweet in self.tweet[followee]:
                all_tweets.append(tweet)
        all_tweets.sort(key=lambda x: x[0], reverse=True)
        return [t[1] for t in all_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)