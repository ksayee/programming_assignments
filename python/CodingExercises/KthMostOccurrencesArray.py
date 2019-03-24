'''
Find k numbers with most occurrences in the given array
Given an array of n numbers and a positive integer k.
The problem is to find k numbers with most occurrences, i.e.,
the top k numbers having the maximum frequency.
If two numbers have same frequency then the larger number should be given preference.
The numbers should be displayed in decreasing order of their frequencies.
It is assumed that the array consists of k numbers with most occurrences.

Examples:

Input : arr[] = {3, 1, 4, 4, 5, 2, 6, 1},
             k = 2
Output : 4 1
Frequency of 4 = 2
Frequency of 1 = 2
These two have the maximum frequency and
4 is larger than 1.

Input : arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9},
            k = 4
Output : 5 11 7 10
'''

def KthMostOccurencesArray(ary,k):

   dict={}
   fnl_lst=[]
   for key in ary:
       if key in dict.keys():
           dict[key]=dict.get(key)+1
       else:
           dict[key]=1
   sort_lst=sorted(dict.items(),key=lambda x:x[1],reverse=True)

   for i in range(0,len(sort_lst)):
       if i<k:
           fnl_lst.append(sort_lst[i][0])
   return fnl_lst

def main():

    ary=[3, 1, 4, 4, 5, 2, 6, 1]
    k=2
    print(KthMostOccurencesArray(ary,k))

    ary = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
    k=4
    print(KthMostOccurencesArray(ary,k))

if __name__=='__main__':
    main()