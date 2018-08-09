# Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
# Given two strings, find if we can make first string from second by deleting some characters from second and rearranging remaining characters.

def getDict(str):

    dict={}

    for i in range(0,len(str)):

        key=str[i]
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    return dict

def CounterDictionary(s1,s2):

    dict1=getDict(s1)
    dict2=getDict(s2)
    flg=True

    for key,val in dict1.items():
        if key in dict2.keys() and val <= dict2.get(key):
            continue
        else:
            flg=False

    if flg==True:
        return "Possible"
    else:
        return "Not Possible"

def main():
    
    s1='ABHISHEKsinGH'
    s2='gfhfBHkooIHnfndSHEKsiAnG'
    print(CounterDictionary(s1,s2))

    s1 = 'Hello'
    s2 = 'dnaKfhelddf'
    print(CounterDictionary(s1, s2))

    s1 = 'GeeksforGeeks'
    s2 = 'rteksfoGrdsskGeggehes'
    print(CounterDictionary(s1, s2))

if __name__=='__main__':
    main()