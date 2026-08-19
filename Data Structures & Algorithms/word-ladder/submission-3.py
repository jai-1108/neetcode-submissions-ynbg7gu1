class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        hashmap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                hashmap[pattern].append(word)
        q = deque()
        q.append(beginWord)
        res = 1
        visited = set()
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in hashmap[pattern]:
                        if neiword not in visited:
                            q.append(neiword)
                            visited.add(neiword)
            res += 1
        return 0

                    
