'''
981. Time Based Key-Value Store
Medium
Create a timebased key-value store class TimeMap, that supports two operations.
1. set(string key, string value, int timestamp)
Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)
Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
Example 1:
Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
'''

class LeetCode981(object):
    def __init__(self):
        self.dict={}

    def set(self,lst):
        key=lst[0]
        val=lst[1]
        time=lst[2]

        if key in self.dict.keys():
            tup=(val,time)
            self.dict[key].append(tup)
        else:
            tup=(val,time)
            self.dict[key]=[]
            self.dict[key].append(tup)

    def get(self,lst):
        key=lst[0]
        time=lst[1]

        if key not in self.dict.keys():
            return 'NONE'
        else:
            flg=False
            val=self.dict[key]
            for i in range(len(val)-1,-1,-1):
                if val[i][1]<=time:
                    flg=True
                    return val[i][0]
            if flg==False:
                return 'NONE'

def main():

    timemap1=LeetCode981()
    timemap1.set(["foo", "bar", 1])
    print(timemap1.get(["foo", 1]))
    print(timemap1.get(["foo", 3]))
    timemap1.set(["foo", "bar2", 4])
    print(timemap1.get(["foo", 4]))
    print(timemap1.get(["foo", 5]))

    timemap2 = LeetCode981()
    timemap2.set(["love", "high", 10])
    timemap2.set(["love", "low", 20])
    print(timemap2.get(["love", 5]))
    print(timemap2.get(["love", 10]))
    print(timemap2.get(["love", 15]))
    print(timemap2.get(["love", 20]))
    print(timemap2.get(["love", 25]))

if __name__=='__main__':
    main()