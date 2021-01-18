'''
1670. Design Front Middle Back Queue
Design a queue that supports push and pop operations in the front, middle, and back.
Implement the FrontMiddleBack class:
FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:
Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
Example 1:
Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]
Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
'''

import math
class FrontMiddleBack(object):
    def __init__(self):
        self.queue = []

    def PushFront(self,value):

        if len(self.queue)==0:
            self.queue.append(value)
        else:
            self.queue.insert(0,value)

    def PushBack(self,value):

        self.queue.append(value)

    def PushMiddle(self,value):

        if len(self.queue)==0:
            self.queue.append(value)
        elif len(self.queue)==1:
            self.queue.insert(0,value)
        else:
            lgt = len(self.queue)
            if lgt % 2 !=0:
                idx = math.floor(lgt/2)
                self.queue.insert(idx,value)
            else:
                idx = lgt//2
                self.queue.insert(idx,value)

    def PopFront(self):

        if len(self.queue)==0:
            print('Empty Queue')
        else:
            self.queue.pop(0)

    def PopBack(self):

        if len(self.queue)==0:
            print('Empty Queue')
        else:
            self.queue.pop()

    def PopMiddle(self):

        if len(self.queue)==0:
            print('Empty Queue')
        else:
            lgt = len(self.queue)
            if lgt%2!=0:
                idx = math.floor(lgt/2)
                del self.queue[idx]
            else:
                idx = lgt//2 -1
                del self.queue[idx]

    def DisplayList(self,action):

        print('Action ' + action + ' : ' + str(self.queue))

def main():

    operations = ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
    number = [1, 2, 3, 4]
    i=0
    for action in operations:
        if action == 'FrontMiddleBackQueue':
            obj = FrontMiddleBack()
            obj.DisplayList(action)
        elif action == 'pushFront':
            obj.PushFront(number[i])
            obj.DisplayList(action)
            if i < len(number)-1:
                i = i +1
        elif action == 'pushBack':
            obj.PushBack(number[i])
            obj.DisplayList(action)
            if i < len(number)-1:
                i = i +1
        elif action == 'pushMiddle':
            obj.PushMiddle(number[i])
            obj.DisplayList(action)
            if i < len(number)-1:
                i = i +1
        elif action == 'popFront':
            obj.PopFront()
            obj.DisplayList(action)
        elif action == 'popBack':
            obj.PopBack()
            obj.DisplayList(action)
        elif action == 'popMiddle':
            obj.PopMiddle()
            obj.DisplayList(action)

if __name__=='__main__':
    main()
