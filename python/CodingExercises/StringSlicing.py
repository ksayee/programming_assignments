# String slicing in Python to check if a string can become empty by recursive deletion
# Given a string “str” and another string “sub_str”. We are allowed to delete “sub_str” from “str” any number of times. It is also given that the “sub_str” appears only once at a time. The task is to find if “str” can become empty by removing “sub_str” again and again.

def StringSlicing(str,sub_str):

    if len(str)==0:
        return False

    while(len(str)!=0):

        idx=str.find(sub_str)

        if idx==-1:
            return False

        str=str[0:idx]+ str[idx+len(sub_str):]

    return True

def main():

    str='GEEGEEKSKS'
    sub_str='GEEKS'
    print(StringSlicing(str,sub_str))

    str = 'GEEGEEKSSGEK'
    sub_str = 'GEEKS'
    print(StringSlicing(str, sub_str))


if __name__=='__main__':
    main()