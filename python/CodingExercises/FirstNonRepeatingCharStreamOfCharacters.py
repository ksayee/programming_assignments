'''
Find the first non-repeating character from a stream of characters
Given a stream of characters, find the first non-repeating character from stream.
You need to tell the first non-repeating character in O(1) time at any moment.
If we follow the first approach discussed here, then we need to store the stream so that we can traverse
it one more time to find the first non-repeating character at any moment. If we use extended approach discussed in the same post,
we need to go through the count array every time first non-repeating element is queried. We can find the first non-repeating character from stream at any moment without traversing any array.
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
The idea is to use a DLL (Doubly Linked List) to efficiently get the first non-repeating character from a stream.
The DLL contains all non-repeating characters in order, i.e., the head of DLL contains first non-repeating character, the second node contains the second non-repeating and so on.
We also maintain two arrays: one array is to maintain characters that are already visited two or more times,
we call it repeated[], the other array is array of pointers to linked list nodes, we call it inDLL[]. The size of both arrays is equal to alphabet size which is typically 256.

Create an empty DLL. Also create two arrays inDLL[] and repeated[] of size 256. inDLL is an array of pointers to DLL nodes.
repeated[] is a boolean array, repeated[x] is true if x is repeated two or more times,
otherwise false. inDLL[x] contains pointer to a DLL node if character x is present in DLL, otherwise NULL.
Initialize all entries of inDLL[] as NULL and repeated[] as false.
To get the first non-repeating character, return character at head of DLL.
Following are steps to process a new character ‘x’ in a stream.
If repeated[x] is true, ignore this character (x is already repeated two or more times in the stream)
If repeated[x] is false and inDLL[x] is NULL (x is seen first time). Append x to DLL and store address of new DLL node in inDLL[x].
If repeated[x] is false and inDLL[x] is not NULL (x is seen second time). Get DLL node of x using inDLL[x] and remove the node. Also, mark inDLL[x] as NULL and repeated[x] as true.
Note that appending a new node to DLL is O(1) operation if we maintain tail pointer. Removing a node from DLL is also O(1).
So both operations, addition of new character and finding first non-repeating character take O(1) time.
'''

import collections

class Solution(object):
    def __init__(self):
        self.dict={}
        self.stk=[]

    def add(self,letter):
        if letter in self.dict.keys():
            self.dict[letter]=self.dict.get(letter)+1
        else:
            self.dict[letter]=1

        if self.dict[letter]==1:
            if len(self.stk)==0:
                self.stk.append(letter)
            else:
                self.stk.append(letter)
        else:
            try:
                idx=self.stk.index(letter)
                del self.stk[idx]
            except:
                pass
        if len(self.stk)==0:
            print('Everything is Repeating')
        else:
            print("First Non-Repeating Character: ",self.stk[0])

def main():
    
    obj=Solution()
    obj.add('g')
    obj.add('g')
    obj.add('e')
    obj.add('e')
    obj.add('k')
    obj.add('g')

if __name__=='__main__':
    main()