'''
Given a String='abc' give all the combinations of string.
'''

def StringCombinations(str,tmp_str,idx,lst):

    for i in range(idx,len(str)):
        tmp_str=tmp_str+str[i]
        lst.append(tmp_str)
        StringCombinations(str,tmp_str,i+1,lst)
        tmp_str=tmp_str[0:-1]

    return lst

def main():

    str='abc'
    lst=[]
    print(sorted(StringCombinations(str,'',0,lst),key=lambda x:len(x)))

    str = 'abcd'
    lst = []
    print(sorted(StringCombinations(str, '', 0, lst),key=lambda x:len(x)))


if __name__=='__main__':
    main()
