# Given a list return a list of random number taht are sorted

import random

def fnl(i):

    return random.random()

def ReturnRandom(ary, n):

    return sorted(ary,key=fnl)[:n]
def main():

    ary = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 5
    print(ReturnRandom(ary, n))

if __name__=='__main__':
    main()