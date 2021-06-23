'''
This problem was asked by Stripe.
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
'''

def FlattenItems_recur(input_dict,output_dict,prev_key):

    for key,val in input_dict.items():
        if isinstance(val,dict):
            FlattenItems_recur(val,output_dict,prev_key + '.' + key)
        else:
            new_key = prev_key + '.' + key
            output_dict[new_key] = val


def DailyCodingProblem925(input_dict):

    print(input_dict)

    output_dict = {}

    for key,val in input_dict.items():
        if isinstance(val,dict):
            FlattenItems_recur(val,output_dict,key)
        else:
            output_dict[key]=val

    return output_dict

def main():

    dict = {}
    dict['key'] = 3
    dict['foo'] = {}
    dict['foo']['a'] =5
    dict['foo']['bar']={}
    dict['foo']['bar']['baz']=8
    print(DailyCodingProblem925(dict))

if __name__=='__main__':
    main()