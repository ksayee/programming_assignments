"""
import pandas
from numpy import NaN

def get_dependencies_df():
    columns = ['object_id', 'object_name', 'depends_on_id', 'depends_on_name']
    values =[(1,2,3,4,5,5,6),
             ('a_0', 'a_1', 'a_2', 'b_0', 'b_1', 'b_1', 'c_0'),
             (NaN,1,2,1,4,3,NaN),
             (NaN,'a_0','a_1','a_0','b_0','a_2',NaN)]



    df=pandas.DataFrame.from_records(values, columns = columns)
    #return DataFrame.from_records(values, columns = columns)


def main():
    get_dependencies_df()

if __name__=='__main__':
    main()
    """
from pandas import DataFrame
from numpy import NaN
import math

def get_dependencies_df() -> DataFrame:
    columns = ('object_id', 'object_name', 'depends_on_id', 'depends_on_name')
    values = \
        [
            [1,    'a_0',    NaN, NaN ],
            [2, 'a_1',     1,    'a_0'],
            [3, 'a_2',     2,    'a_1'],
            [4, 'b_0',     1,    'a_0'],
            [5, 'b_1',     4,    'b_0'],
            [5, 'b_1',     3,    'a_2'],
            [6, 'c_0',     NaN, NaN ]
        ]
    return DataFrame.from_records(values, columns = columns)


def get_depends_on_id(object_id: int):
    df=get_dependencies_df()
    return df[df['object_id'] == object_id]['depends_on_id'].tolist()


def flatten_dict_values(dependency_dict):
    return [val for sublist in dependency_dict.values() for val in sublist]


def get_final_list(current_node, keys):
    final_list = []
    for x in keys:
        if float(x) == float(current_node):
            pass
        elif math.isnan(x):
            pass
        else:
            final_list.append(x)
    return final_list


def get_source_tree(current_node):
    original_node = current_node
    dependency_dict = {}
    dependency_dict[original_node] = get_depends_on_id(original_node)
    print(dependency_dict)
    done_nodes = []
    done_nodes.append(original_node)
    print(done_nodes)
    while not math.isnan(current_node) and not (math.isnan(dependency_dict[current_node][0])):
        for element in flatten_dict_values(dependency_dict):
            print(element)
            if element not in dependency_dict or dependency_dict[element] == []:
                dependency_dict[element] = get_depends_on_id(element)
                done_nodes.append(element)
            else:
                for value in dependency_dict[element]:
                    dependency_dict[value] = []
                    current_node = value

    return get_final_list(original_node, dependency_dict.keys())



def main():
    get_dependencies_df()
    get_source_tree(5)

if __name__=='__main__':
    main()
