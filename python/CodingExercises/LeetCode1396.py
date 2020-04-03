'''
1396. Design Underground System
Implement the class UndergroundSystem that supports three methods:
1. checkIn(int id, string stationName, int t)
A customer with id card equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.
2. checkOut(int id, string stationName, int t)
A customer with id card equal to id, gets out from the station stationName at time t.
3. getAverageTime(string startStation, string endStation)
Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.
Example 1:
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
Output
[null,null,null,null,null,null,null,14.0,11.0,null,11.0,null,12.0]
Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.0
'''

class UndergroundSystem(object):
    def __init__(self):
        self.checkinMap={}
        self.FromToMap={}

    def CheckIn(self,pass_id,from_station,checkIn_time):
        self.checkinMap[pass_id]=[]
        self.checkinMap[pass_id].append(from_station)
        self.checkinMap[pass_id].append(checkIn_time)

    def CheckOut(self,pass_id,to_station,checkOut_time):
        fromStation=self.checkinMap[pass_id][0]
        fromTime=self.checkinMap[pass_id][1]
        del self.checkinMap[pass_id]
        key=fromStation+'|'+to_station
        if key in self.FromToMap.keys():
            self.FromToMap[key][0]=self.FromToMap[key][0]+(checkOut_time-fromTime)
            self.FromToMap[key][1]=self.FromToMap[key][1]+1
        else:
            self.FromToMap[key]=[]
            self.FromToMap[key].append(checkOut_time-fromTime)
            self.FromToMap[key].append(1)

    def GetAverageTime(self,fromStation,toStation):
        key=fromStation+'|'+toStation
        return self.FromToMap[key][0]/self.FromToMap[key][1]

def main():

    ug=UndergroundSystem()
    ug.CheckIn(45, "Leyton", 3)
    ug.CheckIn(32, "Paradise", 8)
    ug.CheckIn(27, "Leyton", 10)
    ug.CheckOut(45, "Waterloo", 15)
    ug.CheckOut(27, "Waterloo", 20)
    ug.CheckOut(32, "Cambridge", 22)
    print(ug.GetAverageTime("Paradise", "Cambridge"))
    print(ug.GetAverageTime("Leyton", "Waterloo"))
    ug.CheckIn(10, "Leyton", 24)
    print(ug.GetAverageTime("Leyton", "Waterloo"))
    ug.CheckOut(10, "Waterloo", 38)
    print(ug.GetAverageTime("Leyton", "Waterloo"))

if __name__=='__main__':
    main()