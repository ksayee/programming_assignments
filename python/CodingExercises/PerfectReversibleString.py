def PerfectReversibleString(str1):

    lst=list(str1)

    lst.reverse()

    if str1==''.join(lst):
        return True
    else:
        return False

def main():

    str1 = 'ab'
    print(PerfectReversibleString(str1))

    str1 = 'aba'
    print(PerfectReversibleString(str1))

    str1 = 'abab'
    print(PerfectReversibleString(str1))

if __name__=='__main__':
    main()