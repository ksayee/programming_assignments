# Find three element from different three arrays such that that a + b + c = sum
# Given three integer arrays and a “sum”, the task is to check if there are three elements a, b, c
# such that a + b + c = sum and a, b and c belong to three different arrays.

def ThreeElementSumThreeArray(a1,a2,a3,k):

    dict={}

    for l in a1:
        if l not in dict.keys():
            dict[l]=1

    fnl_lst=[]
    for i in range(0,len(a2)):
        for j in range(0,len(a3)):

            sum=a2[i]+a3[j]

            diff=k-sum
            if diff in dict.keys():
                tup=(diff,a2[i],a3[j])
                fnl_lst.append(tup)
    return fnl_lst

def main():

    a1=[ 1 , 2 , 3 , 4 , 5]
    a2 = [2 , 3 , 6 , 1 , 2]
    a3 = [3 , 2 , 4 , 5 , 6 ]
    k=9
    print(ThreeElementSumThreeArray(a1,a2,a3,k))

    a1 = [1 , 2 , 3 , 4 , 5]
    a2 = [2 , 3 , 6 , 1 , 2]
    a3 = [3 , 2 , 4 , 5 , 6 ]
    k=20
    print(ThreeElementSumThreeArray(a1, a2, a3,k))

if __name__=='__main__':
    main()