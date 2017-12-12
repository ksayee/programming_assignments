def ReverseArrary(ary):

    st=0
    end=len(ary)-1

    while st<end:
        tmp=ary[st]
        ary[st]=ary[end]
        ary[end]=tmp
        st=st+1
        end=end-1
    print(ary)

def main():
    ary = [1, 2, 3, 4, 5, 6,7]
    ReverseArrary(ary)

if __name__=='__main__':
    main()