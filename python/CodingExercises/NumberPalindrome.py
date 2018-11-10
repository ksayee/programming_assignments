# Check if the brackets in the given string in balanced or not.

def NumberPalindrome(num):

    inp=num

    tmp=[]
    while num!=0:
        rem=num%10
        tmp.append(str(rem))
        num=num//10

    if inp==int(''.join(tmp)):
        return True
    else:
        return False

def main():

    num = 112211
    print(NumberPalindrome(num))
    num = 3344882
    print(NumberPalindrome(num))

if __name__=='__main__':
    main()