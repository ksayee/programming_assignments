# This is question from Cracking the coding interview. Chapter 1.9

def stringrotation(str1,str2):

    if len(str1)!=len(str2):
        return False

    tmp=str1+str1

    if tmp.count(str2)==1:
        return True

def main():
    str1 = 'waterbottle'
    str2 = 'erbottlewat'

    if(stringrotation(str1,str2)):
        print('Strings are rotated')
    else:
        print('Strings are NOT rotated')

if __name__=='__main__':
    main()
