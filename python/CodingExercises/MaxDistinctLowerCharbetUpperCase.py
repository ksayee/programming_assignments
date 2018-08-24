# Maximum distinct lowercase alphabets between two uppercase
# Given a string containing alphabets in lowercase and uppercase, find the maximum count of distinct lowercase alphabets present between two uppercase alphabets.

def MaxDistinctLowerCharbetUpperCase(str1):

    max_cnt=0
    cnt=0
    st=0
    end=0
    flg=False
    tmp=[]
    for i in range(0,len(str1)):

        key=str1[i]

        if key>='A' and key<='Z':
            if flg==False:
                st=i
                flg=True
            else:
                end=i
                if len(tmp)>max_cnt:
                    max_cnt=len(tmp)
                tmp=[]
                st=i
        else:
            if flg==True:
                if key not in tmp:
                    tmp.append(key)

    if cnt>max_cnt:
        max_cnt=cnt
    return max_cnt

def main():

    str1='zACaAbbaazzC'
    print(MaxDistinctLowerCharbetUpperCase(str1))

    str1 = 'edxedxxxCQiIVmYEUtLi'
    print(MaxDistinctLowerCharbetUpperCase(str1))

if __name__=='__main__':
    main()