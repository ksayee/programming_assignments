'''
346. Moving Average from Data Stream
Difficulty: Easy
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
For example,

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

def GetAverage(stk):

    den=len(stk)
    sum=0
    for l in stk:
        sum=sum+l
    return int(sum/den)

def LeetCode346(ary,window):

    fnl_lst=[]
    k=1
    sum=0
    stk=[]
    for i in range(0,len(ary)):
        stk.append(ary[i])
        if len(stk)<=window:
            pass
        else:
            stk.pop(0)
        avg=GetAverage(stk)
        fnl_lst.append(avg)
    return fnl_lst

def main():

    ary=[1,10,3,5]
    window=3
    print(LeetCode346(ary,window))

if __name__=='__main__':
    main()