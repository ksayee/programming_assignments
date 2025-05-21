
class Node(object):
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self,cache_size):
        self.head = None
        self.tail = None
        self.cache_size = cache_size
        self.nodes_cnt = 0

    def addNode(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.nodes_cnt = self.nodes_cnt +1
        else:
            if self.nodes_cnt < self.cache_size:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.nodes_cnt = self.nodes_cnt + 1
            else:
                self.head = self.head.next
                self.head.prev = None

                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode

        return newNode

    def deleteNode(self,node):
        if self.head == node and self.tail == node:
            self.head = None
            self.tail = None
            self.nodes_cnt = 0
            return "Destroy"
        else:
            if self.head == node:
                self.head = self.head.next
                self.head.prev = None
            elif self.tail == node:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.nodes_cnt = self.nodes_cnt -1
            return "DoNothing"

    def print_DLL(self):
        if self.head is None:
            print("Empty Linked List!")
        else:
            node = self.head
            ddl_lst = []
            while node is not None:
                ddl_lst.append(node.value)
                node = node.next
        return ddl_lst

class LFUCache(object):
    def __init__(self,cache_size):
        self.cache_size = cache_size
        self.node_dict = {}
        self.node_freq ={}
        self.freq_dict = {}

    def add(self,value):
        if value not in self.node_dict.keys():
            if 1 in self.freq_dict.keys():
                pass
            else:
                self.freq_dict[1] = DoublyLinkedList(self.cache_size)
            self.node_dict[value] = self.freq_dict[1].addNode(value)
            self.node_freq[self.node_dict[value]] = 1
        else:
            print("Value {value} already present in LFU Cache".format(value = value))
        self.print_LFUCache()

    def get(self,value):
        if value in self.node_dict.keys():
            node = self.node_dict[value]
            prev_node_freq = self.node_freq[node]
            new_node_freq = prev_node_freq + 1
            if new_node_freq in self.freq_dict.keys():
                pass
            else:
                self.freq_dict[new_node_freq] = DoublyLinkedList(self.cache_size)
            self.node_dict[value] = self.freq_dict[new_node_freq].addNode(value)

            response = self.freq_dict[prev_node_freq].deleteNode(node)
            if response == "DoNothing":
                pass
            elif response == "Destroy":
                del self.freq_dict[prev_node_freq]

            del self.node_freq[node]
            self.node_freq[self.node_dict[value]] = new_node_freq
        else:
            print("Value {value} not present in LFU Cache, hence adding!".format(value = value))
            self.add(value)
        self.print_LFUCache()

    def print_LFUCache(self):
        freq_lst = sorted(self.freq_dict.items(),key = lambda x:x[0])

        for item in freq_lst:
            print("Frequence {freq}: {DDL_lst}".format(freq=item[0], DDL_lst = str(item[1].print_DLL())))

def main():

    cache=LFUCache(4)
    cache.add(1)
    cache.add(2)
    cache.add(3)
    cache.add(4)
    cache.add(5)
    cache.get(3)
    cache.get(4)
    cache.get(5)
    cache.add(6)
    cache.add(7)
    cache.get(7)
    cache.get(7)
    cache.get(7)
    cache.add(8)
    cache.get(2)
    cache.get(6)
    cache.get(8)
    cache.add(10)
    cache.add(11)
    cache.add(12)
    cache.add(13)
    cache.add(14)
    cache.add(15)
    cache.get(12)
    cache.get(14)

if __name__=='__main__':
    main()