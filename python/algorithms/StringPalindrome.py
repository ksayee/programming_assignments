def StringPalindrome(str1):

    st=0
    end=len(str1)-1
    flg=True
    while st<end:
        if str1[st]!=str1[end]:
            flg=False
            break
        st=st+1
        end=end-1

    print(flg)

def main():
    str1 = 'malayalam'
    StringPalindrome(str1)

if __name__=='__main__':
    main()