def uniquechar(str1):

    dict={}

    for i in range(0,len(str1)):
        key=str1[i]

        if key in dict.keys():
            return False
        else:
            dict[key]=1

    return True

def main():

    str1 = 'mary'
    print(uniquechar(str1))

    str1 = 'maryr'
    print(uniquechar(str1))


if __name__=='__main__':
    main()