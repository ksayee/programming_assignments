# Change string to a new character set
# Given a 26 letter character set, which is equivalent to character set of English alphabet i.e. (abcd….xyz) and act as a relation. We are also given several sentences and we have to translate them with the help of given new character set.

def ChangeStringCharacter(str,str1):

    lst=list(str)
    print("Original String:", str1)

    fnl_lst=[]

    for i in range(0,len(str1)):
        key=str1[i].lower()
        idx=lst.index(key)

        item=chr(97+idx)
        fnl_lst.append(item)

    return ''.join(fnl_lst)

def main():

    str="qwertyuiopasdfghjklzxcvbnm"
    str1="utta"
    print(ChangeStringCharacter(str,str1))

    str1 = "egrt"
    print(ChangeStringCharacter(str, str1))

if __name__=='__main__':
    main()