'''
Problem Description
Write a function that checks whether two strings are anagrams of each other. A string s1 is an anagram of another string s2 if the same characters exist in both s1 and s2 in any order. For example: "abcd" and "cdab" are anagrams. Also "aabfffr" and "afbfraf" are anagrams.

Sample inputs - Expected outputs
"abcd", "cdab"          -> True
"aabfffr", "afbfraf"    -> True
"kdkd", "dkdr"          -> False
'''

def AnagramBloomberg2(a,b):

    if ''.join(sorted(a))==''.join(sorted(b)):
        return True
    else:
        return False
def AnagramBloomberg1(a,b):

    if len(a)!=len(b):
        return False
    else:
        dict={}
        for key in list(a):
            if key in dict.keys():
                dict[key]=dict.get(key)+1
            else:
                dict[key]=1
        for key in list(b):
            if key in dict.keys() and dict.get(key)>0:
                dict[key]=dict.get(key)-1
            else:
                return False
    return True

def main():

    a='abcd'
    b='cdab'
    print(AnagramBloomberg1(a,b))
    print(AnagramBloomberg2(a, b))

    a = 'aabfffr'
    b = 'afbfraf'
    print(AnagramBloomberg1(a, b))
    print(AnagramBloomberg2(a, b))

    a = 'kdkd'
    b = 'dkdr'
    print(AnagramBloomberg1(a, b))
    print(AnagramBloomberg2(a, b))

if __name__=='__main__':
    main()