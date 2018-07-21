def flattenStack(lst):
    stk=[]
    for i in range(len(lst)-1,-1,-1):
        stk.append(lst[i])
    print(stk)
    stk.pop()
    print(stk)

def flattenlist(lst):
    fnl=[]
    for l in lst:
        if isinstance(l,list):
            fnl.extend(flattenlist(l))
        else:
            fnl.append(l)
    return fnl

def main():
    
    lst=[1,[2,3,4,5],6,7,[8,9,[10,11]]]
    print(flattenlist(lst))
    flattenStack(lst)

if __name__=='__main__':
    main()