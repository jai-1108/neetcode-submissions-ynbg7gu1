class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = {}
            for c in s:
                count[c] = 1 + count.get(c,0)
            res[tuple(sorted(count.items()))].append(s)
        return list(res.values())

        