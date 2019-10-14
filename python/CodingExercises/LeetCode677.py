'''
677. Map Sum Pairs
Implement a MapSum class with insert, and sum methods.
For the method insert, you'll be given a pair of (string, integer).
The string represents the key and the integer represents the value.
If the key already existed, then the original key-value pair will be overridden to the new one.
For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs'
value whose key starts with the prefix.
Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
'''

class MapSum(object):
    def __init__(self):
        self.dict={}

    def Insert(self,key,val):
        if key in self.dict.keys():
            self.dict[key]=self.dict.get(key)+val
        else:
            self.dict[key]=val

    def Sum(self,str1):
        sum=0
        for key,val in self.dict.items():
            if key.startswith(str1):
                sum=sum+val
        return sum
                
def main():

    ms=MapSum()
    ms.Insert("apple", 3)
    print(ms.Sum("ap"))
    ms.Insert("app", 2)
    print(ms.Sum("ap"))

if __name__=='__main__':
    main()