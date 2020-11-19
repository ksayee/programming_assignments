'''
You are given a huge list of airline ticket prices between different cities around the world on a given day. These are all direct flights. Each element in the list has the format (source_city, destination, price).
Consider a user who is willing to take up to k connections from their origin city A to their destination B. Find the cheapest fare possible for this journey and print the itinerary for that journey.
For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:
[
('JFK', 'ATL', 150),
('ATL', 'SFO', 400),
('ORD', 'LAX', 200),
('LAX', 'DFW', 80),
('JFK', 'HKG', 800),
('ATL', 'ORD', 90),
('JFK', 'LAX', 500),
]

Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.

'''

def Flights_recur(value,flights_dict,flight_results,inp_dest,out_sum,path):

    for i in range(0,len(value)):
        key=value[i][0]
        if key==inp_dest:
            path=path+','+key
            out_sum=out_sum+value[i][1]
            tmp=[]
            tmp.append(('-->'.join(path.split(','))))
            tmp.append(out_sum)
            flight_results.append(tmp.copy())
            return
        elif key in flights_dict.keys():
            Flights_recur(flights_dict[key], flights_dict, flight_results, inp_dest, out_sum+value[i][1], path+','+key)
    return

def AirbnbFlights(lst,inp_org,inp_dest):

    flights_dict={}

    for item in lst:
        org=item[0]
        dest=item[1]
        fare=item[2]
        if org in flights_dict.keys():
            flights_dict[org].append((dest,fare))
        else:
            flights_dict[org]=[]
            flights_dict[org].append((dest,fare))

    found=False
    flight_results=[]
    print('Dict Creation Results: '+ str(flights_dict))
    for key,val in flights_dict.items():

        if key==inp_org:
            found=True
            print(val)
            for i in range(0,len(val)):
                out_sum=0
                path = ''
                if val[i][0]==inp_dest:
                    out_sum = out_sum + val[i][1]
                    tmp = []
                    tmp.append((key + '-->' + inp_dest))
                    tmp.append(out_sum)
                    flight_results.append(tmp.copy())
                else:
                    if val[i][0] in flights_dict.keys():
                        out_sum = out_sum + val[i][1]
                        path = key +','+ val[i][0]
                        Flights_recur(flights_dict[val[i][0]],flights_dict,flight_results,inp_dest,out_sum,path)
        else:
            if found==True:
                break
            else:
                pass
    print('Output Results:' + str(flight_results))
    return sorted(flight_results,key=lambda x:x[1])[0]

def main():

    lst=[
('JFK', 'ATL', 150),
('ATL', 'SFO', 400),
('ORD', 'LAX', 200),
('LAX', 'DFW', 80),
('JFK', 'HKG', 800),
('ATL', 'ORD', 90),
('JFK', 'LAX', 500),
('SFO', 'HKG', 400),
]
    org='JFK'
    dest='LAX'
    print(AirbnbFlights(lst,org,dest))

if __name__=='__main__':
    main()