from collections import Counter

def FrequentNumber(ary):
    c=Counter(ary)
    print(sorted(c.items(),key=lambda x:x[0])[-1][0])
    print(c)
def main():
    ary = [0,1,4,4,3]
    FrequentNumber(ary)

if __name__=='__main__':
    main()