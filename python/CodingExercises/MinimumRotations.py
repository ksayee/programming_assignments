def MinimumRotations(str):

    cnt=0
    flg=True
    for i in range(1,len(str)):

        tmp=str[i:]+str[0:i]
        cnt=cnt+1
        if str==tmp:
            break
            flg=False

    if flg==True:
        cnt=cnt+1
    return cnt

def main():

    str1 = 'geeks'
    print(MinimumRotations(str1))

    str1 = 'aaaa'
    print(MinimumRotations(str1))

if __name__=='__main__':
    main()