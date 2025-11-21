
def combinations_recur(lst,cnt,tmp_lst,output_lst,n):

    if len(tmp_lst)==n:
        if ''.join(tmp_lst) not in output_lst:
            output_lst.append(''.join(tmp_lst))

    for i in range(0,len(lst)):
        if cnt[i] == 0:
            continue
        tmp_lst.append(str(lst[i]))
        cnt[i]=cnt[i]-1
        combinations_recur(lst, cnt, tmp_lst, output_lst, n)
        tmp_lst.pop()
        cnt[i]=cnt[i]+1

def Solution(n):

    dict={}
    dict[0]=n
    dict[1]=n

    lst=[]
    cnt=[]
    tmp_lst=[]
    output_lst=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    combinations_recur(lst,cnt,tmp_lst,output_lst,n)
    return output_lst

def main():

    n=3
    print(Solution(n))

if __name__=='__main__':
    main()