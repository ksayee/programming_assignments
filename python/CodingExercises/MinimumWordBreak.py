'''
Minimum Word Break
Given a string s, break s such that every substring of the partition can be found in the dictionary. Return the minimum break needed.
Examples:

Given a dictionary ["Cat", "Mat", "Ca",
     "tM", "at", "C", "Dog", "og", "Do"]

Input :  Pattern "CatMat"
Output : 1
Explanation: we can break the sentences
in three ways, as follows:
CatMat = [ Cat Mat ]  break 1
CatMat = [ Ca tM at ] break 2
CatMat = [ C at Mat ] break 2  so the
         output is: 1

Input : Dogcat
Output : 1
'''

def Validate(str1,ary):
    words=str1.split(',')
    for word in words:
        if word not in ary:
            return False
    return True

def Combinations_recur(tmp,idx,op_idx,input_str,ary,output_lst):

    if idx==len(input_str):
        flg=Validate(''.join(tmp).strip(','),ary)
        if flg==True:
            output_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[op_idx]=input_str[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, input_str,ary,output_lst)

    if idx+1<len(input_str):
        Combinations_recur(tmp, idx+1, op_idx+1, input_str,ary,output_lst)

def MinimumWordBreak(ary, input_str):

    tmp=[0]*len(input_str)*2
    idx=0
    op_idx=0
    output_lst=[]
    Combinations_recur(tmp,idx,op_idx,input_str,ary,output_lst)
    return sorted(output_lst,key=lambda x:len(x))[0]

def main():

    ary=["Cat", "Mat", "Ca","tM", "at", "C", "Dog", "og", "Do"]
    input_str='CatMat'
    print(MinimumWordBreak(ary,input_str))

    input_str = 'DogCat'
    print(MinimumWordBreak(ary, input_str))

if __name__=='__main__':
    main()