class treenote:
    def __init__(self):
        self.children = {}
        self.value = False

class PrefixTree:
    def __init__(self):
        self.root = treenote()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.children:
                cur.children[s] = treenote()
            cur = cur.children[s]
        cur.value = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        return cur.value
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        return True


