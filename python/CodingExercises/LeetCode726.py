'''
726. Number of Atoms
Hard
Given a chemical formula (given as a string), return the count of each atom.
An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
1 or more digits representing the count of that element may follow if the count is greater than 1.
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
'''

def LeetCode726(formula):

    stk=[]
    for i in range(0,len(formula)):
        key=formula[i]
        if key>='A' and key<='Z':
            tmp=[]
            tmp.append(key)
            tmp.append(1)
            stk.append(tmp.copy())
        elif key>='a' and key<='z':
            last_tmp=stk[-1]
            stk.pop()
            tmp=[]
            tmp.append(last_tmp[0]+key)
            tmp.append(1)
            stk.append(tmp.copy())
        elif key>='1' and key<='9':
            if stk[-1]!=')':
                last_tmp=stk[-1]
                stk.pop()
                tmp=[]
                tmp.append(last_tmp[0])
                tmp.append(last_tmp[1]*int(key))
                stk.append(tmp.copy())
            else:
                stk.pop()
                out_lst=[]
                while stk[-1]!='(':
                    last_tmp=stk[-1]
                    tmp=[]
                    tmp.append(last_tmp[0])
                    tmp.append(last_tmp[1]*int(key))
                    out_lst.append(tmp.copy())
                    stk.pop()
                stk.pop()
                while len(out_lst)!=0:
                    stk.append(out_lst[-1].copy())
                    out_lst.pop()
        elif key=='(' or key==')':
            stk.append(key)
    dict={}
    for tup in stk:
        if tup[0] in dict.keys():
            dict[tup[0]]=str(int(dict.get(tup[0]))+tup[1])
        else:
            dict[tup[0]]=str(tup[1])
    for key,val in dict.items():
        if val=='1':
            dict[key]=''

    sort_dict=sorted(dict.items(),key=lambda x:x[0])

    lst=[]
    for tup in sort_dict:
        lst.append(''.join(tup))
    return ''.join(lst)

def main():

    formula = "H2O"
    print(LeetCode726(formula))

    formula = "Mg(OH)2"
    print(LeetCode726(formula))

    formula = "K4(ON(SO3)2)2"
    print(LeetCode726(formula))

if __name__=='__main__':
    main()