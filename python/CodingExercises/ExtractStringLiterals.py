'''
 Implement a function to extract out all string literal from a SQL string return them in a sorted list
def extract_string_literals(str):
    # write your code here
    return str_literal_list
# Sample test cases to verify functionality
assert extract_string_literals("select * from order where orderid = 'OEHKJHFUI' and product = 'Iphone 5s'") = ['Iphone 5s', 'OEHKJHFUI']
assert extract_string_literals("select * from inventory") = []
assert extract_string_literals("select * from order where orderid in ('o1','o2','o1')") = ['o1', 'o1', 'o2']
'''

def ExtractStringLiterals(str1):

    org_str=str1
    flg=True
    cnt=0
    fnl_lst=[]
    st=0
    end=0
    while flg==True:
        try:
            idx=str1.index("'")
            cnt=cnt+1
            if cnt%2!=0:
                if end==0:
                    st=end+idx+1
                else:
                    st=end+idx+1+1
            else:
                end=st+idx
                fnl_lst.append(org_str[st:end])
            str1=str1[idx+1:]
        except:
            break
    return fnl_lst

def main():

    str1="select * from order where orderid = 'OEHKJHFUI' and product = 'Iphone 5s'"
    print(ExtractStringLiterals(str1))

    str1 = "select * from order where orderid in ('o1','o2','o1')"
    print(ExtractStringLiterals(str1))

if __name__=='__main__':
    main()