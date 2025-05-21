
class Node(object):
    def __init__(self,value):
        self.value=value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self,cache_size):
        self.cache_size=cache_size
        self.dict = {}
        self.head = None
        self.tail = None

    def put(self,value):

        if value in self.dict.keys():
            self.get(value)

        else:
            newNode = Node(value)

            if len(self.dict.keys()) < self.cache_size:
                self.dict[value] = newNode
                print('Inserting Value {value}'.format(value=value))

                if self.head is None:
                    self.head = newNode
                    self.tail = newNode
                else:
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.tail = newNode
            else:

                print('Cache is FULL, removing {value}'.format(value = self.head.value))
                del self.dict[self.head.value]
                self.dict[value] = newNode
                print('Inserting Value {value}'.format(value=value))
                self.head = self.head.next
                self.head.prev = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

        self.printCache()
        self.printCache_backwards()

    def get(self,value):

        if value in self.dict.keys():
            print('Getting Value {value}'.format(value=value))
            node = self.dict[value]

            if node == self.tail:
                pass
            elif self.head == node:
                self.head = self.head.next
                self.head.prev = None
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self.tail.next = None

            self.printCache()
            self.printCache_backwards()
        else:
            print('Value {value} is NOT in Cache!!'.format(value = value))

    def printCache(self):
        if self.head is None and self.tail is None:
            print('Cache is EMPTY!!')
        else:
            node = self.head
            while node is not None:
                if node.next is not None:
                    print(node.value,end='-')
                else:
                    print(node.value)
                node = node.next

    def printCache_backwards(self):
        if self.head is None and self.tail is None:
            print('Cache is EMPTY!!')
        else:
            node = self.tail
            while node is not None:
                if node.prev is not None:
                    print(node.value,end='-')
                else:
                    print(node.value)
                node = node.prev

def main():

    cache=LRUCache(5)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    cache.put(4)
    cache.put(5)
    cache.put(6)
    cache.put(7)
    cache.get(6)
    cache.get(1)
    cache.get(3)
    cache.get(7)
    cache.get(3)
    cache.get(7)
    cache.get(4)
    cache.get(1)
    cache.get(2)

if __name__=='__main__':
    main()