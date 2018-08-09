# Generate two output strings depending upon occurrence of character in input string in Python
# Given an input string str[], generate two output strings. One of which consists of those character which occurs only once in input string and second which consists of multi-time occurring characters. Output strings must be sorted.

def getDict(str):

    dict={}

    for i in range(0,len(str)):
        key=str[i]
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    return dict

def CharacterOccurence(s1):

    dict=getDict(s1)

    fnl_lst1=[]
    fnl_lst2=[]

    for key,val in dict.items():
        if val==1:
            fnl_lst1.append(key)
        else:
            fnl_lst2.append(key)

    print("Single Occurence:",''.join(sorted(fnl_lst1)))
    print("Multiple Occurence:", ''.join(sorted(fnl_lst2)))

def main():
    
    s1='geeksforgeeks'
    CharacterOccurence(s1)

    s1 = 'geekspractice'
    CharacterOccurence(s1)

if __name__=='__main__':
    main()