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

class LeetCode460(object):

    def __init__(self,cacheSize):
        self.cacheSize=cacheSize
        self.dict={}
        self.stk=[]
        self.freq={}

    def add(self,value):

        if len(self.dict.keys())<self.cacheSize:
            self.dict[value] = 1
        else:
            sort_freq=sorted(self.freq.items(),key=lambda x:x[0])
            if len(sort_freq[0][1])==1:
                del self.freq[sort_freq[0][0]]
                del self.dict[sort_freq[0][1][0]]
                idx=self.stk.index(sort_freq[0][0])
                del self.stk[idx]
            else:
                del self.dict[sort_freq[0][1][0]]
                self.freq[sort_freq[0][0]].pop(0)
            self.dict[value] = 1

        if 1 in self.freq.keys():
            self.freq[1].append(value)
        else:
            tmp = []
            tmp.append(value)
            self.freq[1] = tmp
            self.stk.append(1)
        self.printCache()

    def get(self,value):

        freq=self.dict[value]
        self.dict[value]=self.dict.get(value)+1

        if len(self.freq[freq])==1:
            del self.freq[freq]
            idx=self.stk.index(freq)
            del self.stk[idx]
        else:
            lst=self.freq[freq]
            idx=lst.index(value)
            del lst[idx]

        if freq+1 in self.freq.keys():
            self.freq[freq+1].append(value)
        else:
            tmp=[]
            tmp.append(value)
            self.freq[freq+1]=tmp
            self.stk.append(freq+1)
        self.printCache()

    def printCache(self):

        if len(self.dict.keys())==0:
            print("Cache is EMPTY")
        else:
            print("Printing LFU Cache")
            for i in range(0,len(self.stk)):
                print("Frequency: ",self.stk[i])
                for j in range(0,len(self.freq[self.stk[i]])):
                    print(self.freq[self.stk[i]][j],end=' ')
                print()

def main():

    cache=LeetCode460(3)
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

if __name__=='__main__':
    main()