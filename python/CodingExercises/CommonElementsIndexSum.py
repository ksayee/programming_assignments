# Minimum Index Sum for Common Elements of Two Lists
# Ram and Shyam want to choose a website to learn programming and they both have a list of favorite websites represented by strings.
# You need to help them find out their common interest with the least index sum. If there is a choice tie between answers, print all of them with no order requirement. Assume there always exists an answer.

def CommonElementsIndexSum(lst1,lst2):

    dict={}

    for l in lst1:
        if l in lst2:
            idx1 = lst1.index(l)
            idx2=lst2.index(l)
            sum=idx2+idx1
            if sum in dict.keys():
                dict[sum].append(l)
            else:
                tmp=[]
                tmp.append(l)
                dict[sum]=tmp

    sort=sorted(dict.items(),key=lambda x:x[0])[0]

    return sort[1]

def main():

    lst1=["GeeksforGeeks", "Udemy", "Coursera", "edX"]
    lst2=["Codecademy", "Khan Academy", "GeeksforGeeks"]
    print(CommonElementsIndexSum(lst1,lst2))

    lst1 = ["Udemy", "GeeksforGeeks", "Coursera", "edX"]
    lst2 = ["GeeksforGeeks", "Udemy", "Khan Academy", "Udacity"]
    print(CommonElementsIndexSum(lst1, lst2))

if __name__=='__main__':
    main()