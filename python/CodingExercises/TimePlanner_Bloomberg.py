'''
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.
Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.
Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.
In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.
Implement an efficient solution and analyze its time and space complexities.
Examples:
input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12
Constraints:
[time limit] 5000ms
[input] array.array.integer slotsA
1 ≤ slotsA.length ≤ 100
slotsA[i].length = 2
[input] array.array.integer slotsB
1 ≤ slotsB.length ≤ 100
slotsB[i].length = 2
[input] integer
[output] array.integer
'''

def GetFlagElement(slotB_sorted, j, dur):

    while j<len(slotB_sorted):
        keyB=slotB_sorted[j]
        if keyB[1]-keyB[0]>=8:
            return (True,j)
        else:
            j=j+1
    return (False,0)

def TimePlanner_Bloomberg(slotA, slotB, dur):
    slotA_sorted = sorted(slotA, key=lambda x: x[0])
    slotB_sorted = sorted(slotB, key=lambda x: x[0])
    j = 0
    flg = True
    result = []
    for i in range(0, len(slotA_sorted)):
        keyA = slotA_sorted[i]
        diff = keyA[1] - keyA[0]
        j = 0
        while diff >= dur:
            tup = GetFlagElement(slotB_sorted, j, dur)
            if tup[0] == True:
                keyB = slotB_sorted[tup[1]]
                if keyA[0] >=keyB[0] and keyA[0]<=keyB[1]:
                    window_start = keyA[0]
                elif  keyB[0] >= keyA[0] and keyB[0]<=keyA[1]:
                    window_start = keyB[0]
                else:
                    window_start=-99
                if window_start!=-99:
                    if keyA[1] <= keyB[1] and keyA[1]>= keyB[0]:
                        window_end = keyA[1]
                    elif keyB[1] <= keyA[1] and keyB[1]>= keyA[0]:
                        window_end = keyB[1]
                    else:
                        window_end=-99
                    if window_end!=-99:
                        if window_end - window_start >= dur:
                            result.append(window_start)
                            result.append(window_start + dur)
                            return result
            else:
                break
            if j < len(slotB_sorted):
                j = j + 1
            else:
                break
    return result

def main():
    slotsA = [[10, 50], [60, 120], [140, 210]]
    slotsB = [[0, 15], [60, 70]]
    dur=8
    print(TimePlanner_Bloomberg(slotsA,slotsB,dur))

    slotsA = [[10, 50], [60, 120], [140, 210]]
    slotsB = [[0, 15], [60, 70]]
    dur = 12
    print(TimePlanner_Bloomberg(slotsA, slotsB, dur))

if __name__=='__main__':
    main()