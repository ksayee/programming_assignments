'''
Create a new string by alternately combining the characters of two halves of the string in reverse
Given a string s, create a new string such that it contains the characters of the two halves of the string s combined alternately in reverse order.
Examples:
Input : s = carbohydrates
Output : hsoebtraarcdy
Input : s = sunshine
Output : sennuish
Explanation:
Example 1: Two halves of the string carbohydrate are carboh and ydrates.
As they needed to be added in reverse alternately, start with h from first half then s from second half followed by o from first half, e from second half and so on.
The string p comes out to be hsoebtraarcdy. If one of the string is completely finished then simply add the remaining characters of the other string in reverse order.
Example 2: The two halves of the string are suns and hine. String sennuish is the desired string p.
'''

def AlternatingCharactersTwoHalvesStringReverse(word):

    half_idx=len(word)//2

    half1=list(word[:half_idx])
    half2=list(word[half_idx:])
    output_list=[]

    flg=True
    while len(half1)!=0 or len(half2)!=0:
        if flg==True:
            if len(half1)>0:
                output_list.append(half1[-1])
                half1.pop()
            flg=False
        else:
            if len(half2)>0:
                output_list.append(half2[-1])
                half2.pop()
            flg=True
    return ''.join(output_list)

def main():

    word='carbohydrates'
    print(AlternatingCharactersTwoHalvesStringReverse(word))

    word = 'sunshine'
    print(AlternatingCharactersTwoHalvesStringReverse(word))

if __name__=='__main__':
    main()