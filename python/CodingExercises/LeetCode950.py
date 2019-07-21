'''
950. Reveal Cards In Increasing Order
Medium
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.
Initially, all the cards start face down (unrevealed) in one deck.
Now, you do the following steps repeatedly, until all cards are revealed:
Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.
The first entry in the answer is considered to be the top of the deck.
Example 1:
Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation:
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
'''

import collections

def Validate(tmp):

    lst=[]
    chk_lst=tmp.copy()
    while True:
        lst.append(tmp[0])
        tmp.pop(0)
        if len(tmp) == 0:
            break
        first_element=tmp[0]
        tmp.pop(0)
        tmp.append(first_element)

    if lst==sorted(chk_lst):
        return True
    else:
        return False

def Combinations_recur(lst,cnt,tmp,fnl_lst,lgt):

    if len(tmp)==lgt:
        flg=Validate(tmp.copy())
        if flg==True:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, lgt)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode950(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,len(ary))
    return fnl_lst

def main():

    ary=[17,13,11,2,3,5,7]
    print(LeetCode950(ary))

if __name__=='__main__':
    main()