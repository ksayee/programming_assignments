'''
Rearrange characters in a string such that no two adjacent are same
Given a string with repeated characters, task is rearrange characters in a string so that no two adjacent characters are same.

Note : It may be assumed that the string has only lowercase English alphabets.

Examples:

Input: aaabc
Output: abaca

Input: aaabb
Output: ababa

Input: aa
Output: Not Possible

Input: aaaabc
Output: Not Possible
'''
class PriorityQueue(object):

    def __init__(self):
        self.stk=[]
        self.dict={}
        self.freq={}

    def push(self,val):

        if val in self.dict.keys():
            self.dict[val]=self.dict.get(val)+1
        else:
            self.dict[val]=1

    def createQueue(self):

        sort_lst=sorted(self.dict.items(),key=lambda x:x[1])

        for key in sort_lst:
            freq_num=key[1]
            val=key[0]

            if freq_num in self.freq.keys():
                self.freq[freq_num].append(val)
            else:
                tmp=[]
                tmp.append(val)
                self.freq[freq_num]=tmp

            if freq_num not in self.stk:
                self.stk.append(freq_num)

    def pop(self):

        freq_num_1=self.stk[-1]
        fnl_lst=[]
        if len(self.freq[freq_num_1])>1:
            tup_1=(self.freq[freq_num_1][0],freq_num_1)
            tup_2=(self.freq[freq_num_1][1],freq_num_1)
            fnl_lst.append(tup_1)
            fnl_lst.append(tup_2)
        else:
            tup_1=(self.freq[freq_num_1][0],freq_num_1)
            if len(self.stk)>1:
                freq_num_2=self.stk[-2]
                tup_2 = (self.freq[freq_num_2][0], freq_num_2)
                fnl_lst.append(tup_1)
                fnl_lst.append(tup_2)
            else:
                fnl_lst.append(tup_1)

        return fnl_lst

    def push_queue(self,fnl_lst):

        for key in fnl_lst:
            if len(key)==0:
                continue
            else:
                if self.dict[key[0]]!=key[1]:
                    if key[1]==0:
                        del self.dict[key[0]]
                    else:
                        self.dict[key[0]]=key[1]
                        freq_num=key[1]

                    if key[1]!=0:
                        if freq_num in self.freq.keys():
                            self.freq[freq_num].append(key[0])
                        else:
                            tmp=[]
                            tmp.append(key[0])
                            self.freq[freq_num]=tmp
                        if freq_num not in self.stk:
                            self.stk.append(freq_num)

                    freq_num=key[1]+1
                    if len(self.freq[freq_num])>1:
                        idx=self.freq[freq_num].index(key[0])
                        del self.freq[freq_num][idx]
                    else:
                        del self.freq[freq_num]
                        if freq_num in self.stk:
                            idx=self.stk.index(freq_num)
                            del self.stk[idx]


    def RearrangeCharacters(self,str1):

        lst=list(str1)

        for i in range(0,len(lst)):
            self.push(lst[i])
        self.createQueue()

        i=0
        tmp=[]
        while i<len(lst):
            fnl_lst=self.pop()
            if len(tmp)==0:
                tmp.append(fnl_lst[0][0])
                tup=(fnl_lst[0][0],fnl_lst[0][1]-1)
                del fnl_lst[0]
                fnl_lst.append(tup)
            else:
                if tmp[-1]==fnl_lst[0][0]:
                    if len(fnl_lst)>1:
                        tmp.append(fnl_lst[1][0])
                        tup = (fnl_lst[1][0], fnl_lst[1][1] - 1)
                        del fnl_lst[1]
                        fnl_lst.append(tup)
                    else:
                        tmp=[]
                        break
                else:
                    tmp.append(fnl_lst[0][0])
                    tup = (fnl_lst[0][0], fnl_lst[0][1] - 1)
                    del fnl_lst[0]
                    fnl_lst.append(tup)
            self.push_queue(fnl_lst)
            i=i+1

        if len(tmp)>1:
            return ''.join(tmp)
        else:
            return 'NO String'

def main():

    str1='aaaadbcd'
    stk=PriorityQueue()
    print(stk.RearrangeCharacters(str1))

    str1 = 'aaabc'
    stk = PriorityQueue()
    print(stk.RearrangeCharacters(str1))

    str1 = 'aaabb'
    stk = PriorityQueue()
    print(stk.RearrangeCharacters(str1))

    str1 = 'aa'
    stk = PriorityQueue()
    print(stk.RearrangeCharacters(str1))

    str1 = 'aaaabc'
    stk = PriorityQueue()
    print(stk.RearrangeCharacters(str1))


if __name__=='__main__':
    main()