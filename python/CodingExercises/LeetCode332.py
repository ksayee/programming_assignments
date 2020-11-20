'''
332. Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure
and arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

def Flights_recur(inp_key,inp_val,flights_dict,tmp):

    for i in range(0,len(inp_val)):
        if inp_val[i]=='X':
            pass
        else:
            key=inp_val[i]
            tmp.append(inp_key)
            flights_dict[inp_key][i]='X'
            if key in flights_dict.keys():
                Flights_recur(key,flights_dict[key],flights_dict,tmp)
            else:
                tmp.append(key)

def GetFlightDict(tickets):
    flights_dict = {}

    for ticket in tickets:
        if ticket[0] in flights_dict.keys():
            flights_dict[ticket[0]].append(ticket[1])
        else:
            flights_dict[ticket[0]] = []
            flights_dict[ticket[0]].append(ticket[1])
    return flights_dict

def LeetCode332(tickets,start_loc):

    flights_dict=GetFlightDict(tickets)

    print("Input Flight Tickets: "+str(flights_dict))
    flight_results=[]

    found=False
    for key,val in flights_dict.items():

        if key==start_loc:
            found=True
            tmp_val=val.copy()
            for i in range(0,len(val)):
                tmp=[]
                tmp.append(key)
                if val[i] in flights_dict.keys():
                    Flights_recur(val[i],flights_dict[val[i]],flights_dict,tmp)
                flight_results.append('-->'.join(tmp.copy()))
                flights_dict=GetFlightDict(tickets)
                val=tmp_val.copy()

        else:
            if found==True:
                break
            else:
                pass
    return flight_results

def main():

    tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(LeetCode332(tickets,'JFK'))

    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(LeetCode332(tickets,'JFK'))

if __name__=='__main__':
    main()