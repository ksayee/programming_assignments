def minabsdiff(ary):

    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            key=abs(ary[i]-ary[j])
            if i==0:
                min=key
            elif key<min:
                min=key
    print(min)

def main():
    ary=[30,5,20,9]

    minabsdiff(ary)

if __name__=='__main__':
    main()
