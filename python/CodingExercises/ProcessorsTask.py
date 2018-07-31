# Given a list of processors and Tasks, Allocate Tasks to processors so that they run completely on one processor. A Task can't be broken into multiple processors. Return a list of processors and the tasks which are running on it.ValidNumber.py
def add_dict(dict,tmp_prs,tmp_tsk,prs_dict):

    tmp_tup=(tmp_prs[0],prs_dict[tmp_prs[0]])
    if tmp_tup in dict.keys():
        dict[tmp_tup].append(tmp_tsk)
    else:
        tmp_lst=[]
        tmp_lst.append(tmp_tsk)
        dict[tmp_tup]=tmp_lst
    return dict

def ProcessorsTask(prs,tsk):

    prs_sort=sorted(prs,key=lambda x:x[1],reverse=True)
    prs_dict={}
    for l in prs_sort:
        if l[0] not in prs_dict.keys():
            prs_dict[l[0]]=l[1]

    tsk_sort = sorted(tsk, key=lambda x:x[1], reverse=True)
    print("Processors:",prs_sort)
    print("Tasks:",tsk_sort)

    dict={}

    for i in range(0,len(tsk_sort)):
        tmp_tsk=tsk_sort[i]
        for j in range(0,len(prs_sort)):
            tmp_prs=prs_sort[j]
            if tmp_tsk[1]<=tmp_prs[1]:
                tmp_val=tmp_prs[1]-tmp_tsk[1]
                if tmp_val==0:
                    dict=add_dict(dict,tmp_prs,tmp_tsk,prs_dict)
                    del prs_sort[j]
                else:
                    tmp_tup=(tmp_prs[0],tmp_val)
                    prs_sort[j]=tmp_tup
                    dict = add_dict(dict, tmp_prs, tmp_tsk,prs_dict)
                break
    return dict

def main():

    prs=[("prs_1",5),("prs_2",10),("prs_3",15),("prs_4",3)]
    tsk=[("tsk_1",3),("tsk_2",2),("tsk_3",3),("tsk_4",13),("tsk_5",1),("tsk_6",5),("tsk_7",5)]

    dict=ProcessorsTask(prs,tsk)
    print("Output Dictionary")
    for key,val in dict.items():
        print("Key, Value:",key,val)

if __name__=='__main__':
    main()