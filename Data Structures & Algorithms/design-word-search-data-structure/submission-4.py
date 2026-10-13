class TreeNote():
    def __init__(self) -> None:
        self.children = {}
        self.value = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNote()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                node = TreeNote()
                cur.children[s] = node
            cur = cur.children[s]
        cur.value = True

                
        

    def search(self, word: str) -> bool:
        cur = self.root
        leng = len(word)

        def dfs(cur,i):
            if i == leng:
                return cur.value
            s = word[i]
            if s == ".":
                for note in cur.children.values():
                    if dfs(note,i+1):
                        return True
                return False
            else:
                if s not in cur.children:
                    return False
                else:
                    return dfs(cur.children[s],i+1)
        return dfs(cur,0)
        
