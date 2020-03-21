'''
Given a list of countries and salaries, give the top two salaries for every country
'''

def Solution(ary):

    dict={}
    for tup in ary:
        key=tup[0]
        val=tup[1]

        if key in dict.keys():
            dict[key].append(tup[1])
        else:
            dict[key]=[]
            dict[key].append(tup[1])
    output_lst=[]

    for key,val in dict.items():
        tmp=[]
        tmp.append(key)
        val.sort(reverse=True)
        if len(val)==1:
            tup=(val[0])
        else:
            tup=(val[:2])
        tmp.append(tup)
        output_lst.append(tmp.copy())
    return output_lst

def main():

    ary=[('IND',1000),('IND',2000),('IND',3000),('US',500),('US',800),('US',1000),('AUS',1000),('AUS',2000),('AUS',1500),('CN',800),('BR',500),('BR',800),('BR',750),]
    print(Solution(ary))

if __name__=='__main__':
    main()