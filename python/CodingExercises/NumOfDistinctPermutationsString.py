# Write a program to give the total number of distinct permutations of a string.

import collections

def Factorial(n):

    if n==1:
        return 1
    res=n*Factorial(n-1)
    return res


def NumOfDistinctPermutationsString(str1):

    dict=collections.Counter(str1)
    numerator=Factorial(len(str1))
    denominator=1
    for key, val in dict.items():
        denominator=denominator * Factorial(val)
    return int(numerator/denominator)

def main():

    str1='aaabbc'
    print(NumOfDistinctPermutationsString(str1))

if __name__=='__main__':
    main()