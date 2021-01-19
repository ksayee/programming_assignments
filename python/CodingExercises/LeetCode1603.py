'''
1603. Design Parking System
Design a parking system for a parking lot.
The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
Implement the ParkingSystem class:
ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to
get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
Example 1:
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]
Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
'''

class ParkingSystem(object):
    def __init__(self,lst):
        for i in range(0,len(lst)):
            if i==0:
                self.big_car = lst[i]
            elif i==1:
                self.medium_car = lst[i]
            elif i==2:
                self.small_car = lst[i]

    def AddCar(self,car_type):

        if car_type==1:
            if self.big_car>0:
                self.big_car=self.big_car-1
            else:
                return False
        elif car_type==2:
            if self.medium_car>0:
                self.medium_car=self.medium_car-1
            else:
                return False
        elif car_type==3:
            if self.small_car>0:
                self.small_car=self.small_car-1
            else:
                return False
        return True

def main():

    input_actions = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    input_values = [[1, 1, 0], [1], [2], [3], [1]]
    i=0
    for action in input_actions:
        if action=='ParkingSystem':
            obj=ParkingSystem(input_values[i])
            i=i+1
        elif action=='addCar':
            print(obj.AddCar(input_values[i][0]))
            if i < len(input_values)-1:
                i=i+1

if __name__=='__main__':
    main()