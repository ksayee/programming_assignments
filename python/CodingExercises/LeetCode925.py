'''
925. Long Pressed Name
Easy
Your friend is typing his name into a keyboard.
Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.
Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
'''

def Compression(word):

    lst=[]
    prev=word[0]
    cnt=1
    for i in range(1,len(word)):
        curr=word[i]
        if curr!=prev:
            lst.append(prev)
            lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    lst.append(prev)
    lst.append(str(cnt))
    return ''.join(lst)

def LeetCode925(name, typed):

    compress_name=Compression(name)
    compress_typed=Compression(typed)

    for i in range(0,len(compress_name)):
        try:
            val=int(compress_name[i])
            if val>int(compress_typed[i]):
                return False
            else:
                pass
        except:
            pass
    return True

def main():

    name = "alex"
    typed = "aaleex"
    print(LeetCode925(name,typed))

    name = "saeed"
    typed = "ssaaedd"
    print(LeetCode925(name, typed))

    name = "leelee"
    typed = "lleeelee"
    print(LeetCode925(name, typed))

    name = "laiden"
    typed = "laiden"
    print(LeetCode925(name, typed))

if __name__=='__main__':
    main()