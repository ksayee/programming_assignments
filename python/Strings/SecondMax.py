
def secondmax(ary):

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]
        elif ary[i]<max:
            if i==1:
                sec_max=ary[i]
            elif ary[i]>sec_max:
                sec_max=ary[i]
        elif ary[i]>max:
            sec_max=max
            max=ary[i]

    print(max)
    print(sec_max)

def secondmin(ary):

    for i in range(0,len(ary)):
        if i==0:
            min=ary[i]
        elif ary[i]>min:
            if i==1:
                sec_min=ary[i]
            elif ary[i]<sec_min:
                sec_min=ary[i]
        elif ary[i]<min:
            sec_min=min
            min=ary[i]

    print(min)
    print(sec_min)

def main():
    ary = [3, 4, 8, 1, 5, -2, 43]
    secondmax(ary)
    secondmin(ary)

if __name__=='__main__':
    main()
