'''
Given a stream of data which contains the session_id, user_id, step_no. and the start time of the step.
Find the average time spent on each step.
Note: there are 4 steps and the  5th step  event is the time when the 4th step was completed successfully.
Input:
import datetime
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
def StreamDataFindAvgTimeSpentEachStep(stream):

    output_dict={}
    result={}
    for element in stream:
        session_id=element[0]
        user_id=element[1]
        step=element[2]
        step_time=element[3]

        if (session_id,user_id,step-1) in output_dict.keys():
            diff = (step_time - output_dict[(session_id, user_id, step - 1)]).total_seconds()
            if step-1 in result.keys():
                result[step-1].append(diff)
            else:
                result[step-1]=[]
                result[step-1].append(diff)
        output_dict[(session_id,user_id,step)]=step_time

    for key,val in result.items():
        total_time=sum(val)
        print('Average Time Spent at Step ' +str(key)+' : ',total_time/len(val))

def main():

    stream=[
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
    StreamDataFindAvgTimeSpentEachStep(stream)

if __name__=='__main__':
    main()