'''
# Given a list of tuples, give me the connected components
# lst=[('a','b'),('b','c'),('a','e'),('c','d'),('f','g'),('h','g')]
'''

def InsertDictionary(key,val,dictionary):

    if key in dictionary.keys():
        dictionary[key].append(val)
    else:
        dictionary[key]=[]
        dictionary[key].append(val)
    return dictionary

def CheckDict(chk_lst,tmp):

    for l in chk_lst:
        if l not in tmp:
            return False
    return True

def GetConnections(value,tmp,dictionary):

    for val in value:
        if val in dictionary.keys():
            chk_lst=[]
            chk_lst.append(val)
            chk_lst.extend(dictionary[val])
            flg=CheckDict(chk_lst,tmp)
            if flg==False:
                tmp.extend(dictionary[val])
                GetConnections(dictionary[val], tmp, dictionary)
            else:
                return
    return

def CheckElement(key,fnl_lst):

    for tup in fnl_lst:
        if key in tup:
            return True
    return False

def ConnectedComponents(lst):

    dict={}
    rev_dict={}

    for tup in lst:
        dict=InsertDictionary(tup[0],tup[1],dict)
        rev_dict=InsertDictionary(tup[1],tup[0],rev_dict)

    fnl_lst=[]

    for key,val in dict.items():
        flg=CheckElement(key,fnl_lst)
        if flg==False:
            tmp=[]
            tmp.append(key)
            tmp.extend(val)
            GetConnections(val,tmp,dict)
            for element in list(set(tmp)):
                if element in rev_dict.keys():
                    tmp.extend(rev_dict[element])
                    GetConnections(rev_dict[element], tmp, rev_dict)
            fnl_lst.append(list(sorted(set(tmp))).copy())

    return fnl_lst

def main():

    lst = [('a', 'b'), ('b', 'c'), ('a', 'e'), ('c', 'd'), ('f', 'g'), ('h', 'g'), ('k', 'a'), ('b', 'a')]
    print('Input')
    print(lst)
    print('Output')
    print(ConnectedComponents(lst))

    lst = [('a', 'b'), ('b', 'a'), ('c', 'e'), ('e', 'd'), ('d', 'c')]
    print('Input')
    print(lst)
    print('Output')
    print(ConnectedComponents(lst))

    lst = [('a', 'bb'), ('bb', 'c'), ('aa', 'e'), ('cc', 'd'), ('cc', 'f'), ('g', 'f')]
    print('Input')
    print(lst)
    print('Output')
    print(ConnectedComponents(lst))

if __name__=='__main__':
    main()