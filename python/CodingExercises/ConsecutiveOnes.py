# Maximum length of consecutive 1’s in a binary string in Python using Map function

def ConsecutiveOnes(str):

    max=-99

    lst=list(str)
    flg=True
    cnt=0
    for l in lst:
        if l=='1':
            cnt=cnt+1
            flg=True
        else:
            if flg == True:
                if cnt > max:
                    max = cnt
            flg=False
            cnt=0
    if cnt>max:
        max=cnt

    return max

def main():

    str = '110001111010101111111'
    print(ConsecutiveOnes(str))

    str = '11000111101010111'
    print(ConsecutiveOnes(str))

if __name__ == "__main__":
    main()
