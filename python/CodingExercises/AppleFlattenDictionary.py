'''
assert flatten({"a": {"b": [1, 2]}, "c": [100, 101], "d": {"f": 200}}) == \
    {"a.b.0": 1, "a.b.1": 2, "c.0": 100, "c.1": 101, "d.f": 200}
assert flatten({"a": 1}) == {"a": 1}

'''

def insertIntoOutputDict(key, val_lst, output_dict):

    if isinstance(val_lst, list) or isinstance(val_lst, tuple):
        for i in range(0,len(val_lst)):
            out_key = key + '.' + str(i)
            out_val = val_lst[i]
            output_dict[out_key] = out_val
    elif isinstance(val_lst, int):
        out_key = key
        out_val = val_lst
        output_dict[out_key] = out_val

def flatten_recur(out_key, out_val_dict, output_dict):

    for key, val in out_val_dict.items():
        if isinstance(val, dict):
            out_key = out_key + '.' + str(key)
            out_val_dict = val
            flatten_recur(out_key, out_val_dict, output_dict)
        elif isinstance(val, list) or isinstance(val, tuple) or  isinstance(val, int):
            out_key = out_key + '.' + str(key)
            insertIntoOutputDict(out_key, val, output_dict)

def solution(input_dict):

    output_dict={}

    for key, val in input_dict.items():

        if isinstance(val, dict):
            out_key = key
            out_val_dict = val
            flatten_recur(out_key, out_val_dict, output_dict)
        elif isinstance(val, list) or isinstance(val, tuple) or isinstance(val, int):
            insertIntoOutputDict(key, val, output_dict)

    return output_dict

def main():

    input_dict = {"a": {"b": [1, 2]}, "c": [100, 101], "d": {"f": 200}}
    print(solution(input_dict))

    input_dict = {"a": {"b": [1, 2]}}
    print(solution(input_dict))

    input_dict = {"a": 1}
    print(solution(input_dict))

if __name__=='__main__':
    main()