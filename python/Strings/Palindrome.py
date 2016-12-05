
def palindrome(ary):

    st=0
    end=len(ary)-1

    while st<end:
        if ary[st]!=ary[end]:
            return False
        st=st+1
        end=end-1
    return True


def main():
    str1='malayalam'
    print('Is the Input string Palindrome? ',palindrome(str1))

if __name__=='__main__':
    main()
