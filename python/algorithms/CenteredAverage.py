def CenteredAverage(ary):

    tot_len=len(ary)
    high=max(ary)
    low=min(ary)

    tot=0

    for i in range(0,len(ary)):
        tot=tot+ary[i]

    ans=int((tot-high-low)/(tot_len-2))

    print(ans)


def main():

    ary=[1,2,3,4,100]
    CenteredAverage(ary)

    ary = [1, 1,5,5,10,8,7]
    CenteredAverage(ary)

    ary = [-10,-4,-2,-4,-2,0]
    CenteredAverage(ary)

if __name__=='__main__':
    main()