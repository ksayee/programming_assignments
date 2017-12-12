import re
import datetime
import json

def return_data(data,log_name):

    dict={}

    dict["Log_file_name"]=log_name

    lst=data.split('\n')

    start_time=lst[0].split(" ")[0]+ " " + lst[0].split(" ")[1]
    dict["Start_Time_Est"] = start_time

    end_time = lst[len(lst) - 2].split(" ")[0] + " " + lst[len(lst) - 2].split(" ")[1]
    dict["End_Time_Est"] = end_time

    datetime_t1=datetime.datetime.strptime(start_time,"%m/%d/%Y %H:%M:%S:%f")
    datetime_t2 = datetime.datetime.strptime(end_time, "%m/%d/%Y %H:%M:%S:%f")
    diff = datetime_t2 - datetime_t1
    session_length=round(diff.total_seconds()/(60*60),1)
    dict["Session_length"]=session_length

    err_cnt=0
    port_cnt=0

    for line in lst:
        if "Timezone" in line:
            time_zone=line[line.find("Timezone to")+len("Timezone to")+1:]
            dict["Time_zone"]=time_zone
        elif "-E" in line:
            err_cnt=err_cnt+1
        elif "cpt_server started with" in line:
            st=line.find("users")+len("users/")
            tmp_line=line[line.find("users")+len("users/"):]

            user_name=line[st:st+tmp_line.find("/")]
            dict["User_Name"]=user_name

            client_version=line[line.find("cmlib"):].split(" ")[0]
            dict["Client_Version"]=client_version
        elif "Gathering Portfolio View" in line:
            if port_cnt==0:
                dict["Portfolios_Loaded"]=[]
            tmp_data=line.split(" ")
            dict["Portfolios_Loaded"].append(tmp_data[len(tmp_data)-1][1:-1])
            port_cnt=port_cnt+1

    dict["Error_Count"]=err_cnt

    print(dict)

def main():

    path="C:/Users/sayeek/Downloads/codetest/codetest/logs/log_sample_1.log"
    f=open(path,'r')
    data=f.read()
    return_data(data,path.split('/')[7])

    path = "C:/Users/sayeek/Downloads/codetest/codetest/logs/log_sample_2.log"
    f = open(path, 'r')
    data = f.read()
    return_data(data, path.split('/')[7])

    path = "C:/Users/sayeek/Downloads/codetest/codetest/logs/log_sample_3.log"
    f = open(path, 'r')
    data = f.read()
    return_data(data, path.split('/')[7])

if __name__=='__main__':
    main()

