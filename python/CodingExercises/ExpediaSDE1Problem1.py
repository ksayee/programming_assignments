'''
Given an array of strings such as:
["A1B","C2","34B","5F6","7","A _ 78K87","65ABC7","0"]
'''

def ExpediaSDE1Problem1(ary):

    fnl_lst=[]
    tmp=[]

    for key in ary:
        lst=list(key)
        tmp=[]
        for l in lst:
            if l>='0' and l<='9':
                tmp.append(l)
            else:
                if len(tmp)>0:
                    fnl_lst.append(int(''.join(tmp)))
                    tmp=[]
        if len(tmp)>0:
            fnl_lst.append(int(''.join(tmp)))
    return fnl_lst

def main():

    ary=["A1B","C2","34B","5F6","7","A _ 78K87","65ABC7","0"]
    print(ExpediaSDE1Problem1(ary))

if __name__=='__main__':
    main()