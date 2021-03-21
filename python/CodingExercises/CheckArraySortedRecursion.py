
def Check_recur(ary):

    if len(ary)==1:
        return True
    if ary[0]<ary[1]:
        flg =Check_recur(ary[1:])
        if flg is True:
            return True
    else:
        return False

def CheckArraySortedRecursion(ary):

    flg = False
    flg = Check_recur(ary)
    if flg is True:
        return True
    else:
        return False

def main():

    ary=[127,220,246,277,321,454,534,565,933]
    print(CheckArraySortedRecursion(ary))

    ary = [127, 220, 246, 80, 321, 454, 534, 565, 933]
    print(CheckArraySortedRecursion(ary))

if __name__=='__main__':
    main()