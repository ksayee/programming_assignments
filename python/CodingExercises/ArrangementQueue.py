'''
Find the arrangement of queue at given time
n people are standing in a queue to buy entry ticket for the carnival.
People present there strongly believe in chivalry.
Therefore, at time = t, if a man at position x,
finds a woman standing behind him then he exchanges his position with her and therefore,
at time = t+1, woman is standing at position x while man is standing behind her.
Given the total number of people standing in a queue as n,
particular instant of time as t and the initial arrangement of the queue in the form of a
string containing ‘M’ representing man at position i and ‘W’ representing
woman is at position i, find out the arrangement of the queue at time = t.
Examples :
Input : n = 6, t = 2
       BBGBBG
Output: GBBGBB
Explanation:
At t = 1, 'B' at position 2 will swap
with 'G' at position 3 and 'B' at
position 5 will swap with 'G' at
position 6. String after t = 1 changes
to "BGBBGB". Now at t = 2, 'B' at
position = 1 will swap with 'G' at
position = 2 and 'B' at position = 4
will swap with 'G' at position 5.
String changes to "GBBGBB". Since,
we have to display arrangement at
t = 2, the current arrangement is
our answer.
Input : n = 8, t = 3
       BBGBGBGB
Output: GGBGBBBB
'''

def ArrangementQueue(str1,t):

    lst=list(str1)

    while t>0:
        for i in range(1,len(lst)):
            if lst[i]=='G' and lst[i-1]=='B':
                lst[i-1]='G'
                lst[i]='B'
        t=t-1
    return ''.join(lst)

def main():

    str1='BBGBBG'
    t=2
    print(ArrangementQueue(str1,t))

    str1 = 'BBGBGBGB'
    t = 3
    print(ArrangementQueue(str1, t))

if __name__=='__main__':
    main()