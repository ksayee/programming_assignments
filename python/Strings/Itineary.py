
def itineary():

    lst={}
    lst['Chennai']='Bangalore'
    lst['Bombay']='Delhi'
    lst['Goa']='Chennai'
    lst['Delhi']='Goa'

    for key,val in lst.items():
        print(key,val)

    rev_lst={}

    for key,val in lst.items():
        rev_lst[val]=key
    print('Reverse')
    print('')

    for key,val in rev_lst.items():
        print(key,val)

    for key,val in lst.items():
        if val in rev_lst.keys():
            start=val

    to=lst.get(start)
    print(to)
    while to!=None:
        print(start,' -- > ',to,',')
        start=to
        to=lst.get(start)



def main():

    itineary()


if __name__=='__main__':
    main()
