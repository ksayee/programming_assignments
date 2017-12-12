def UnionIntersectList(lst1,lst2):

    dict={}

    for i in range(0,len(lst1)):
        key=lst1[i]
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    int=[]
    for j in range(0,len(lst2)):
        key=lst2[j]
        if key in dict.keys():
            int.append(str(lst2[j]))
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    un=[]
    for key,val in dict.items():
        while val>0:
            un.append(str(key))
            val=val-1
    print(un)
    print(int)

def main():
    lst1 = [1, 3, 4, 5, 7]
    lst2 = [2, 3, 5, 6]

    UnionIntersectList(lst1, lst2)

if __name__=='__main__':
    main()