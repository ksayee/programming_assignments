'''
 Given an array and integer m, had to find average of m groups in O(n).

   Ex : A[] = {1, 2, 3, 4, 5}, m = 3
      ans : avg(1,2,3), avg(2,3,4), avg(3,4,5)
'''

def FindAverageMGroups(ary,m):

    avg_lst=[]
    tmp=[]
    cnt=0
    for i in range(0,len(ary)):
        if cnt<m:
            tmp.append(ary[i])
            cnt=cnt+1
            if cnt==m:
                avg_lst.append(sum(tmp)/m)
        else:
            tmp.pop(0)
            tmp.append(ary[i])
            avg_lst.append(sum(tmp)/m)
    return avg_lst
def main():

    ary=[1, 2, 3, 4, 5]
    m=3
    print(FindAverageMGroups(ary,m))

if __name__=='__main__':
    main()