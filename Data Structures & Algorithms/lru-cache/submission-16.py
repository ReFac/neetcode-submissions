class ListNode:
    def __init__(self,val,prev=None,next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.dummy = ListNode(-1)
        self.c = capacity
        self.count = 0
        self.last = self.dummy

    def MoveToEnd(self, key) -> None:
        if key in self.dic:
            node = self.dic[key]
            if node.next:
                pr = node.prev
                nxt =node.next
                pr.next = nxt
                nxt.prev = pr
                node.prev = self.last
                node.next = None
                self.last.next = node
                self.last = node
        

    def get(self, key: int) -> int:
        if key in self.dic:
            self.MoveToEnd(key)
            return self.dic[key].val[1]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = (key,value)
            self.MoveToEnd(key)
        elif self.count < self.c:
            self.count +=1
            x = ListNode((key,value),self.last)
            self.last.next = x
            self.last = x
            self.dic[key] = x
        else:
            node = ListNode((key,value))
            nxt = self.dummy.next
            self.dummy.next = nxt.next
            nxt.next = None
            nxt.prev = None
            self.dic.pop(nxt.val[0])
            if self.c == 1:
                self.last = self.dummy
            else:
                self.dummy.next.prev = self.dummy
            node.prev = self.last
            self.last.next = node
            self.last = node
            self.dic[key] = node
            

            