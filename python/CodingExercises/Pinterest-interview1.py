'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.



Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Input: s = "catsdog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: true
'''

def Validate(new_str,wordDict):
    for word in new_str.split(','):
        if word not in wordDict:
            return False
    return True

def combinations_recur(tmp,input_str,wordDict,idx,op_idx,output_lst):

    if idx == len(input_str):
        flg = Validate(''.join(tmp).strip(','),wordDict)
        if flg is True:
            output_lst.append(''.join(tmp).strip(','))
        return

    tmp[op_idx]=input_str[idx]
    tmp[op_idx+1]=','
    combinations_recur(tmp, input_str, wordDict, idx+1, op_idx+2, output_lst)

    if op_idx+1<=len(input_str):
        combinations_recur(tmp, input_str, wordDict, idx+1, op_idx+1, output_lst)

def solution(input_str, wordDict):
    tmp=[0] * (len(input_str)*2)
    print(tmp)
    idx=0
    op_idx=0
    output_lst=[]

    combinations_recur(tmp,input_str,wordDict,idx,op_idx,output_lst)

    if len(output_lst)==0:
        return False
    else:
        return output_lst

def main():
    input_str = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution(input_str, wordDict))

    input_str = "catsdog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(solution(input_str, wordDict))

if __name__ == '__main__':
    main()