'''
Maximum distinct lowercase alphabets between two uppercase
Given a string containing alphabets in lowercase and uppercase,
find the maximum count of distinct lowercase alphabets present between two uppercase alphabets.
Examples :
Input : zACaAbbaazzC
Output : The maximum count = 3

Input : edxedxxxCQiIVmYEUtLi
Output : The maximum count = 1
'''

def MaxDistinctLowerCaseCharactersBetween2UpperCase(str1):

    upper_flag=False
    max_count=0
    dict={}
    count=0
    for i in range(0,len(str1)):
        key=str1[i]

        if key>='A' and key<='Z':
            if upper_flag==False:
                upper_flag=True
            else:
                if count>0:
                    if count > max_count:
                        max_count=count
                    count=0
                    dict={}
        else:
            if upper_flag==True:
                if key not in dict.keys():
                    dict[key]=1
                    count=count+1
    return max_count

def main():
    
    str1='zACaAbbaazzC'
    print(MaxDistinctLowerCaseCharactersBetween2UpperCase(str1))

    str1 = 'edxedxxxCQiIVmYEUtLi'
    print(MaxDistinctLowerCaseCharactersBetween2UpperCase(str1))

if __name__=='__main__':
    main()