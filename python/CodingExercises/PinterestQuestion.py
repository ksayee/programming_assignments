
def shortest_path(categories, source, destination):
    queue=[]

    queue.append(source)

    output_lst=[]
    visited=[]
    visited.append(source)

    while len(queue)!=0:

        item = queue[0]
        queue.pop(0)

        for key,val in categories.items():
            if item not in val:
                continue
            else:

                for element in val:
                    if element == destination:
                        output_lst.append(element)
                        return output_lst
                    else:
                        if element not in visited:
                            visited.append(element)
                            queue.append(element)

    return None

categories = {
    "Category1": ["mountain", "lake", "hotel"],
    "Category2": ["house", "pond", "hotel"],
    "Category3": ["lodge", "lake"]
}

print(shortest_path(categories, "mountain", "lake"))
print(shortest_path(categories, "mountain", "house"))
print(shortest_path(categories, "pond", "lodge"))
print(shortest_path(categories, "mountain", "lodge"))


