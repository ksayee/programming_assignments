'''
460. LFU Cache
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
Follow up:
Could you do both operations in O(1) time complexity?
Example:
LFUCache cache = new LFUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LeetCode460(object):
    def __init__(self,cacheSize):
        self.dict={}
        self.cacheSize=cacheSize
        self.head=None
        self.tail=None

    def put(self,value):
        newNode=Node(value)

        if self.head==None:
            self.head=newNode
            self.tail=newNode
            self.dict[value] = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            if len(self.dict.keys())<self.cacheSize:
                self.dict[value] = newNode
            else:
                del self.dict[self.head.value]
                self.dict[value]=newNode
                self.head=self.head.next
                self.head.prev=None
        self.printCache()

    def get(self,value):

        if value in self.dict.keys():
            node=self.dict[value]
            if node==self.tail:
                pass
            elif node==self.head:
                self.head = self.head.next
                self.head.prev=None
                node.prev=self.tail
                self.tail.next=node
                node.next=None
                self.tail=node
            else:
                node.prev.next=node.next
                node.next.prev=node.prev
                self.tail.next=node
                node.next = None
                self.tail=node
        self.printCache()

    def printCache(self):

        node=self.head

        if node==None:
            print('Cache is EMPTY')
        else:
            print('Printing Cache')
            while node!=None:
                print(node.value,end=' ')
                node=node.next
        print()

def main():

    cache=LeetCode460(5)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    cache.put(4)
    cache.put(5)
    cache.put(6)
    cache.put(7)
    cache.get(6)
    cache.get(3)
    cache.get(7)
    cache.get(3)
    cache.get(7)
    cache.get(4)

if __name__=='__main__':
    main()