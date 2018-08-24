# Print all words matching a pattern in CamelCase Notation Dictonary
# Given a dictionary of words where each word follows CamelCase notation, print all words in the dictionary that match with a given pattern consisting of uppercase characters only.

def CamelChar(str):

    lst=[]
    for i in range(0,len(str)):
        key=str[i]
        if key>='A' and key<='Z':
            lst.append(key)

    return ''.join(lst)

def WordsCamelCaseDictionary(dict,ptr):

    fnl_lst=[]

    for l in dict:
        cc=CamelChar(l)

        if len(ptr)==len(cc):
            if ptr==cc:
                fnl_lst.append(l)
        elif len(ptr)<len(cc):
            n=len(ptr)
            if ptr==cc[:n]:
                fnl_lst.append(l)

    if len(fnl_lst)>0:
        return fnl_lst
    else:
        return 'No Match'

def main():

    dict=["Hi", "Hello", "HelloWorld",  "HiTech", "HiGeek","HiTechWorld", "HiTechCity", "HiTechLab"]

    ptr='HT'
    print(WordsCamelCaseDictionary(dict,ptr))

    ptr = 'H'
    print(WordsCamelCaseDictionary(dict, ptr))

    ptr = 'HTC'
    print(WordsCamelCaseDictionary(dict, ptr))

    dict = ["WelcomeGeek","WelcomeToGeeksForGeeks", "GeeksForGeeks"]

    ptr = 'WTG'
    print(WordsCamelCaseDictionary(dict, ptr))

    ptr = 'GFG'
    print(WordsCamelCaseDictionary(dict, ptr))

    ptr = 'GG'
    print(WordsCamelCaseDictionary(dict, ptr))

if __name__=='__main__':
    main()