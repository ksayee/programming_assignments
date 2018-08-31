# Group Shifted String
# Given an array of strings (all lowercase letters),
# the task is to group them in such a way that all strings in a group are shifted versions of each other.
# Two string S and T are called shifted if,
# S.length = T.length
# and
# S[i] = T[i] + K for
# 1 <= i <= S.length  for a constant integer K

def GroupShiftedString(ary):

    dict={}

    for key in ary:

        diff_lst=[]
        for i in range(0,len(key)-1):
            diff=ord(key[i+1])-ord(key[i])
            diff_lst.append(str(diff))

        if len(diff_lst)>0:

            if ''.join(diff_lst) in dict.keys():
                dict[''.join(diff_lst)].append(key)
            else:
                tmp=[]
                tmp.append(key)
                dict[''.join(diff_lst)]=tmp
        else:
            if str(1) in dict.keys():
                dict[str(1)].append(key)
            else:
                tmp=[]
                tmp.append(key)
                dict[str(1)]=tmp

    return dict

def main():

    ary=["acd", "dfg", "wyz", "yab", "mop","bdfh", "a", "x", "moqs"]
    print(GroupShiftedString(ary))

if __name__=='__main__':
    main()