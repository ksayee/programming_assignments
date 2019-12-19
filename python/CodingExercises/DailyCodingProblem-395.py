'''
Given an array of strings, group anagrams together.
For example, given the following array:
['eat', 'ate', 'apt', 'pat', 'tea', 'now']
Return:
[['eat', 'ate', 'tea'],
 ['apt', 'pat'],
 ['now']]
'''

def DailyCodingProblem395(ary):

    dict={}
    output_list=[]

    for word in ary:
        key=''.join(sorted(word))
        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key]=[]
            dict[key].append(word)
    for key,val in dict.items():
        output_list.append(val.copy())
    return sorted(output_list,key=lambda x:len(x),reverse=True)

def main():

    ary=['eat', 'ate', 'apt', 'pat', 'tea', 'now']
    print(DailyCodingProblem395(ary))

if __name__=='__main__':
    main()