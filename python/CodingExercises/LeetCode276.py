'''
276. Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1
   5         c2     c1     c2
   6         c2     c2     c1
'''

def LeetCode276(n,k):

    i=1

    lst=[]
    cnt = []
    while i<=k:
        lst.append('c'+str(i))
        i=i+1
        cnt.append(k)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp,n)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp,n):

    if len(tmp)==n:
        fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp,n)
        tmp.pop()
        cnt[i]=cnt[i]+1
            
def main():

    n=3
    k=2
    print(LeetCode276(n,k))

if __name__=='__main__':
    main()