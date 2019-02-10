'''
Write code to return average time taken for each step, when the input is stream of Arrays of size 3 where
first values is session id, second is step2 and third is time stamp.
You have to maintain an existing average time for each step and then calculate average time on the fly using input Array.
streams = [
             [1000, 123, 1, datetime.datetime(2014, 4, 11, 8, 0)]
            ,[1000, 123, 2, datetime.datetime(2014, 4, 11, 8, 10)]
            ,[1000, 123, 3, datetime.datetime(2014, 4, 11, 8, 20)]
            ,[1000, 123, 4, datetime.datetime(2014, 4, 11, 8, 30)]
            ,[1000, 123, 5, datetime.datetime(2014, 4, 11, 8, 31)]
            ,[1001, 125, 1, datetime.datetime(2014, 4, 11, 9, 10)]
            ,[1001, 125, 2, datetime.datetime(2014, 4, 11, 9, 30)]
            ,[1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 50)]
            ,[1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 51)]
            ,[1001, 125, 4, datetime.datetime(2014, 4, 11, 9, 52)]
            ,[1005, 129, 1, datetime.datetime(2014, 4, 11, 9, 8)]
            ,[1005, 129, 2, datetime.datetime(2014, 4, 11, 9, 10)]
            ,[1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 12)]
            ,[1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 13)]
            ,[1005, 129, 4, datetime.datetime(2014, 4, 11, 9, 14)]
            ,[1005, 129, 5, datetime.datetime(2014, 4, 11, 9, 18)]
          ]
'''

import datetime
def GetAverageTimeFB(streams):

    dict={}

    for lst in streams:
        cust=lst[1]
        step=lst[2]
        time=lst[3]

        if cust in dict.keys():
            if step in dict[cust].keys():
                if lst[3]<dict[cust][step]:
                    dict[cust][step]=lst[3]
            else:
                dict[cust][step]=lst[3]
        else:
            tmp={}
            tmp[step]=lst[3]
            dict[cust]=tmp
    for key,val in dict.items():
        print(key,val)

    sort_dict={}
    for key,val in dict.items():
        tmp=[]
        for key1,val1 in val.items():
            tup=(key1,val1)
            tmp.append(tup)
        sort_dict[key]=sorted(tmp.copy(),key=lambda x:x[0])

    res_dict={}
    for key,val in sort_dict.items():
        tmp={}
        for i in range(1,len(val)):
            step=val[i-1][0]
            diff=(val[i][1]-val[i-1][1]).total_seconds()
            tmp[step]=diff
        res_dict[key]=tmp

    for key,val in res_dict.items():
        print(key,val)

    fnl_dict={}
    for key,val in res_dict.items():
        for key1,val1 in val.items():
            if key1 in fnl_dict.keys():
                fnl_dict[key1].append(val1)
            else:
                tmp=[]
                tmp.append(val1)
                fnl_dict[key1]=tmp
    for key,val in fnl_dict.items():
        print(key,val)

    avg_lst=[]
    for key,val in fnl_dict.items():
        sum=0
        for l in val:
            sum=sum+l
        tup=(key,sum/len(val))
        avg_lst.append(tup)
    return avg_lst

def main():
    streams = [
          [1000, 123, 1, datetime.datetime(2014, 4, 11, 8, 0)]
        , [1000, 123, 2, datetime.datetime(2014, 4, 11, 8, 10)]
        , [1000, 123, 3, datetime.datetime(2014, 4, 11, 8, 20)]
        , [1000, 123, 4, datetime.datetime(2014, 4, 11, 8, 30)]
        , [1000, 123, 5, datetime.datetime(2014, 4, 11, 8, 31)]
        , [1001, 125, 1, datetime.datetime(2014, 4, 11, 9, 10)]
        , [1001, 125, 2, datetime.datetime(2014, 4, 11, 9, 30)]
        , [1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 50)]
        , [1001, 125, 3, datetime.datetime(2014, 4, 11, 9, 51)]
        , [1001, 125, 4, datetime.datetime(2014, 4, 11, 9, 52)]
        , [1005, 129, 1, datetime.datetime(2014, 4, 11, 9, 8)]
        , [1005, 129, 2, datetime.datetime(2014, 4, 11, 9, 10)]
        , [1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 12)]
        , [1005, 129, 3, datetime.datetime(2014, 4, 11, 9, 13)]
        , [1005, 129, 4, datetime.datetime(2014, 4, 11, 9, 14)]
        , [1005, 129, 5, datetime.datetime(2014, 4, 11, 9, 18)]
    ]
    print(GetAverageTimeFB(streams))

if __name__=='__main__':
    main()