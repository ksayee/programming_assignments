"""
Context/Prompt:
Listings on Airbnb usually represent a single bookable unit of inventory. For some listings such as hotels, there are many bookable units of inventory. For those, listings can be created at levels beyond bookable inventory (e.g., at the property level). These form a parent-child relationship where properties of the parent are ‘accessible’ by the children (e.g., if the building has a common swimming pool, all units also have access to the swimming pool).
For the purposes of this exercise, assume there is a max depth of 3 for listing hierarchies (i.e., a listing can have a parent and a grandparent).

Consider a data structure that is a list of tuples which holds pairs of listing ids to denote (parent listing, child listing). e.g., [(1,5), (1,6), (3,4), (2,3)] → 1 and 2 are top-level parents.

You also have map of listing_ids (int) to attributes (set) to denote what amenities are present in a listing (note how the parent listings contain more general shared amenities that the child listings can also access):
example:
amenities_dict = {
  1: {"bbq_area", "lobby", "swimming_pool"},
  2: {"ballroom"},
  3: {"elevator", "parking_garage"},
  4: {"wifi", "table"},
  5: {"toaster_oven", "kitchen", "toilet"},
  6: {"standing_desk", "hammock"}
}

Write a method in the language of your choice that will take two inputs (list of tuples and a map) and update the map so that the child listing inherits the attributes of the parent listings, showing the complete list of attributes each listing has. For example, listing 5 should have six attributes in total in the final map.
Example output:
{
1: {'swimming_pool', 'bbq_area', 'lobby'},
2: {'ballroom'},
3: {'ballroom', 'parking_garage', 'elevator'},
4: {'elevator', 'wifi', 'parking_garage', 'table', 'ballroom'},
5: {'swimming_pool', 'bbq_area', 'lobby', 'kitchen', 'toilet', 'toaster_oven'},
6: {'hammock', 'standing_desk', 'bbq_area', 'lobby', 'swimming_pool'}
}
"""



def recur(val,key,child_parent_dict,result_dict):

    if val in child_parent_dict.keys():
        for val1 in child_parent_dict[val]:
            if val1 not in result_dict[key]:
                result_dict[key].append(val1)
                recur(val1, key, child_parent_dict, result_dict)
    return

def solution(relationships,amenities_dict):

    child_parent_dict={}

    for item in relationships:
        if item[1] in child_parent_dict.keys():
            child_parent_dict[item[1]].append(item[0])
        else:
            child_parent_dict[item[1]]=[]
            child_parent_dict[item[1]].append(item[0])

    print('Child Parent Dictionary:',child_parent_dict)

    result_dict={}

    for key,val in child_parent_dict.items():

        result_dict[key]=[]

        for val1 in val:
            result_dict[key].append(val1)
            recur(val1,key,child_parent_dict,result_dict)

    print('Child with All ancestors dict:',result_dict)

    for key,val in amenities_dict.items():
        tmp=list(val)

        if key in result_dict.keys():
            for item in result_dict[key]:
                lst = tmp + list(set(amenities_dict[item]))
                tmp= lst.copy()

        amenities_dict[key]=set(tmp)

    return amenities_dict

def main():

    relationships = [(1, 5), (1, 6), (3, 4), (2, 3)]
    amenities_dict = {
        1: {"bbq_area", "lobby", "swimming_pool"},
        2: {"ballroom"},
        3: {"elevator", "parking_garage"},
        4: {"wifi", "table"},
        5: {"toaster_oven", "kitchen", "toilet"},
        6: {"standing_desk", "hammock"}
    }
    print(solution(relationships,amenities_dict))

if __name__=='__main__':
    main()
