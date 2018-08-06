# Find one extra character in a string
# Given two strings which are of lengths n and n+1. The second string contains all the character of the first string, but there is one extra character. Your task to find the extra character in the second string..

def ExtraCharacter(str1,str2):

    if len(str1)>len(str2):
        big_str=str1
        sml_str=str2
    else:
        big_str=str2
        sml_str=str1
    dict={}

    for i in range(0,len(big_str)):
        key=big_str[i]

        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    for i in range(0,len(sml_str)):
        key=sml_str[i]

        if key in dict.keys():
            dict[key]=dict.get(key)-1
    for key, val in dict.items():
        if val==0:
            continue
        else:
            print("Extra Character:",key,val)

def main():

    str1="abcd"
    str2="cdbae"
    ExtraCharacter(str1,str2)

    str1 = "kxml"
    str2 = "klxml"
    ExtraCharacter(str1, str2)

if __name__=='__main__':
    main()