'''
1324. Print Words Vertically
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"
Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed.
"TBONTB"
"OEROOE"
"   T"
Example 3:
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
'''

def LeetCode1324(str1):

    lst=str1.split(' ')
    stk=[]
    dict={}
    i=0
    for word in lst:
        stk.append(i)
        dict[i]=list(word)
        i=i+1

    output_lst=[]
    while True:
        word=[]
        for key in stk:
            if len(dict[key])>0:
                word.append(dict[key][0])
                dict[key].pop(0)
            else:
                word.append(' ')
        if ''.join(word).replace(' ','')!='':
            output_lst.append(''.join(word))
        else:
            break
    return output_lst

def main():

    str1 = "HOW ARE YOU"
    print(LeetCode1324(str1))

    str1 = "TO BE OR NOT TO BE"
    print(LeetCode1324(str1))

    str1 = "CONTEST IS COMING"
    print(LeetCode1324(str1))

if __name__=='__main__':
    main()