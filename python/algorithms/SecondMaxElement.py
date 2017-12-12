def SecondMaxElement(ary):

    sec_max_ele=ary[0]
    max_ele=ary[0]

    for i in range(1,len(ary)):
        if ary[i]>max_ele:
            sec_max_ele=max_ele
            max_ele=ary[i]
        elif ary[i]>sec_max_ele:
            sec_max_ele=ary[i]
        else:
            continue

    print(sec_max_ele)

def main():

    ary=[5,89,20,64,20,45,53]
    SecondMaxElement(ary)

if __name__=='__main__':
    main()