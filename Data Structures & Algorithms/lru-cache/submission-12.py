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
        

    def get(self, key: int) -> int:
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

            return self.dic[key].val[1]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = (key,value)
            if node.next:
                pr = node.prev
                nxt =node.next
                pr.next = nxt
                nxt.prev = pr
                node.prev = self.last
                node.next = None
                self.last.next = node
                self.last = node
        elif self.count < self.c:
            self.count +=1
            x = ListNode((key,value),self.last)
            self.last.next = x
            self.last = x
            self.dic[key] = x
        else:
            x = ListNode((key,value),self.last)
            self.last.next = x
            self.last = x
            self.dic[key] = x

            nxt = self.dummy.next
            self.dummy.next = nxt.next
            nxt.next = None
            nxt.prev = None
            self.dummy.next.prev = self.dummy

            self.dic.pop(nxt.val[0], None)