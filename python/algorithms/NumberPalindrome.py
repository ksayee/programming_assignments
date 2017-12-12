def NumberPalindrome(num):

    tmp=num
    rev_num=0
    while tmp!=0:
        rev_num=rev_num*10+tmp%10
        tmp=int(tmp/10)
    if num==rev_num:
        print(True)
    else:
        print(False)

def main():
    num=112211
    NumberPalindrome(num)

    num = 3344882
    NumberPalindrome(num)

if __name__=='__main__':
    main()