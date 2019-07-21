'''
1000. Minimum Cost to Merge Stones
Hard
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.
A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.
Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.
Example 1:
Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:
Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:
Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
'''

def CheckConsecutive(tmp,stone_string):

    tmp_str=[]
    for l in tmp:
        tmp_str.append(str(l))
    try:
        idx=stone_string.index(''.join(tmp_str))
    except:
        return False
    return True

def GetCost(tmp,stones,k):

    new_ary=[]
    for l in stones:
        if l not in tmp:
            new_ary.append(l)
    cost=0
    for l in tmp:
        cost=cost+l
    new_ary.append(cost)

    while len(new_ary)!=1:
        if len(new_ary)>=k:
            new_ary.sort()
            i=0
            sum=0
            while i<k:
                sum=sum+new_ary[i]
                i=i+1
            i=0
            while i<k:
                new_ary.pop(0)
                i=i+1
            cost=cost+sum
            new_ary.append(sum)
        else:
            return -1
    return cost

def Combinations_recur(lst,cnt,tmp,fnl_lst,k,stones,stone_string):

    if len(tmp)==k:
        flg=CheckConsecutive(tmp,stone_string)
        if flg==True:
            cost=GetCost(tmp,stones,k)
            if cost in fnl_lst.keys():
                if sorted(tmp) not in fnl_lst[cost]:
                    fnl_lst[cost].append(sorted(tmp.copy()))
            else:
                fnl_lst[cost]=[]
                fnl_lst[cost].append(sorted(tmp.copy()))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, k,stones,stone_string)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode1000(stones, k):

    lst=stones
    cnt=[]
    for i in range(0,len(stones)):
        cnt.append(1)
    tmp=[]
    fnl_lst={}
    stone_str=[]
    for stone in stones:
        stone_str.append(str(stone))

    Combinations_recur(lst,cnt,tmp,fnl_lst,k,stones,''.join(stone_str))
    return sorted(fnl_lst.items(),key=lambda x:x[0])[0][0]

def main():

    stones = [3, 2, 4, 1]
    k = 2
    print(LeetCode1000(stones,k))

    stones = [3,2,4,1]
    k = 3
    print(LeetCode1000(stones, k))

    stones = [3,5,1,2,6]
    k = 3
    print(LeetCode1000(stones, k))

if __name__=='__main__':
    main()