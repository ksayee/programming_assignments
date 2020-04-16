'''
 two string are given had to find the missing string
    Ex - String one - "This is an example"
           String two - "is example"
         ans - This, an
'''

def FindMissingWordsInBothStrings(str1,str2):

    lst1=str1.split(' ')
    lst2=str2.split(' ')
    return (set(lst1)-set(lst2)) | (set(lst2)-set(lst1))

def main():

    str1='This is an example'
    str2='is kartik example'
    print(FindMissingWordsInBothStrings(str1,str2))

if __name__=='__main__':
    main()