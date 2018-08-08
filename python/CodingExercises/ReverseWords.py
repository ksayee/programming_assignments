# Reverse words in a given String in Python
# We are given a string and we need to reverse words of given string ?

def ReverseWords(str1):

    fnl_lst=str1.split()

    fnl_lst.reverse()

    return ' '.join(fnl_lst)

def main():

    str1='geeks quiz practice code'
    print(ReverseWords(str1))


if __name__=='__main__':
    main()