def issomorphic(str1,str2):

    if len(str1)!=len(str2):
        return False

    dict={}

    for i in range(0,len(str1)):
        key=str1[i]
        if key in dict.keys():
            if str2[i]!=dict.get(key):
                return False
        else:
            for key,val in dict.items():
                if val==str2[i]:
                    return False
            dict[key]=str2[i]
    return True


def main():
    str1='aac'
    str2='xxy'
    if issomorphic(str1,str2)==True:
        print('Strings are Issomorphic')
    else:
        print('Strings are NOT Issomorphic')

if __name__=='__main__':
    main()
