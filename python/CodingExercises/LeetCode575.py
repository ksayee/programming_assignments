'''
575. Distribute Candies

Given an integer array with even length,
where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
'''

def LeetCode575(ary):

    ary_lgt=len(ary)
    unq_lgt=len(set(ary))

    hlf=ary_lgt/2

    if hlf==unq_lgt:
        return unq_lgt
    else:
        if hlf<unq_lgt:
            return unq_lgt-1
        else:
            return unq_lgt


def main():

    ary=[1,1,2,2,3,3]
    print(LeetCode575(ary))

    ary = [1,1,2,3]
    print(LeetCode575(ary))

    ary = [1, 1, 1, 1, 1, 1, 2, 3]
    print(LeetCode575(ary))

    ary = [1, 1, 1, 1, 1, 1, 2,2,2,2,2, 3]
    print(LeetCode575(ary))


if __name__=='__main__':
    main()