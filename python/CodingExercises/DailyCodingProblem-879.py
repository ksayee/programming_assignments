'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def DailyCodingProblem879_sol1(lst,target):

    dict={}

    for element in lst:
        if target-element in dict.keys():
            return (element,target-element)
        else:
            dict[element]=1
    return 'No combination'

def DailyCodingProblem879_sol2(lst,target):

    lst.sort()

    idx=-1
    for i in range(0,len(lst)):

        element = target-lst[i]

        left=0
        right =len(lst)-1

        flg=False
        while left < right:
            mid = (left+right)//2
            if lst[mid]==element:
                flg= True
                idx=mid
                break
            elif element < lst[mid]:
                right= mid -1
            elif element> lst[mid]:
                left=mid+1
        if flg==False:
            idx=-1

        if idx==-1:
            pass
        else:
            return (lst[i],element)
            break
    return 'No combination'

def main():

    lst=[10, 15, 3, 7]
    target =17
    print(DailyCodingProblem879_sol1(lst,target))

    lst = [10, 15, 3, 7]
    target = 17
    print(DailyCodingProblem879_sol2(lst, target))

if __name__=='__main__':
    main()