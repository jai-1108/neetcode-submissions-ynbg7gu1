class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)
        
        rows = len(board)
        cols = len(board[0])
        res = set()
        path = set()

        def dfs(r,c,word,node):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in path or board[r][c] not in node.children:
                return
            path.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_end:
                res.add(word)
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)
            path.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,"",root)
        return list(res)