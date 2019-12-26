'''
Print all valid words that are possible using Characters of Array
Given a dictionary and a character array, print all valid words that are possible using characters from the array.

Examples:

Input : Dict - {"go","bat","me","eat","goal",
                                "boy", "run"}
        arr[] = {'e','o','b', 'a','m','g', 'l'}
Output : go, me, goal.

'''
import collections

def Validate(tmp,word):

    if ''.join(tmp) in word:
        return True
    else:
        return False

def Combinations_recur(lst,cnt,tmp,fnl_lst,word):

    if len(tmp)>0:
        flg=Validate(tmp,word)
        if flg==True:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, word)
        cnt[i]=cnt[i]+1
        tmp.pop()

def PrintValidWordFromArray(word,ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,word)
    return fnl_lst

def main():

    word=["go","bat","me","eat","goal", "boy", "run"]
    ary=['e','o','b', 'a','m','g', 'l']
    print(PrintValidWordFromArray(word,ary))

if __name__=='__main__':
    main()