'''
Input:
User activity count over the past 7 days.
0 is non active on that day on that device
1 is active on that day on that device

device_dt_list = {'ChromeWeb' : [1,0,0,1,1,1,0],
                   'iOS': [1,0,0,1,1,1,0],
                   'androidOS': [1,0,0,1,0,1,0],
                  'Firefox' : [0,0,1,1,0,1,0]
                   }

rollup = {'overall': ['ChromeWeb', 'iOS', 'androidOS', 'Firefox'],
           'mobile' : ['iOS', 'androidOS']}
'''

def SevenDayActiveUserCount(device_dict,rollup_dict):
    fnl_lst=[]
    for key,val in rollup_dict.items():
        tmp=[]
        for device in val:
            dev_val=device_dict[device]
            if len(tmp)==0:
                tmp=dev_val
            else:
                for i in range(0,len(dev_val)):
                    if (dev_val[i]==1 and tmp[i]==1) or (dev_val[i]==0 and tmp[i]==1) or (dev_val[i]==1 and tmp[i]==0):
                        tmp[i]=1
        sum=0
        for i in range(0,len(tmp)):
            sum=sum+tmp[i]
        tup=(key,sum)
        fnl_lst.append(tup)
    return fnl_lst

def main():
    device_dict = {'ChromeWeb': [1, 0, 0, 1, 1, 1, 0],
                      'iOS': [1, 0, 0, 1, 1, 1, 0],
                      'androidOS': [1, 0, 0, 1, 0, 1, 0],
                      'Firefox': [0, 0, 1, 1, 0, 1, 0]
                      }
    rollup_dict = {'overall': ['ChromeWeb', 'iOS', 'androidOS', 'Firefox'],
              'mobile': ['iOS', 'androidOS']}
    print(SevenDayActiveUserCount(device_dict,rollup_dict))

if __name__=='__main__':
    main()