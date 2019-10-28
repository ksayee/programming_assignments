'''
# Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID.

# The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

# For example:
# logs = [
#     ["58523", "user_1", "resource_1"],
#     ["62314", "user_2", "resource_2"],
#     ["54001", "user_1", "resource_3"],
#     ["215", "user_6", "resource_4"],
#     ["200", "user_6", "resource_5"],
#     ["54060", "user_2", "resource_3"],
#     ["53941", "user_3", "resource_3"],
#     ["58522", "user_4", "resource_1"],
#     ["53651", "user_5", "resource_3"],
#     ["2", "user_6", "resource_1"],
#     ["100", "user_6", "resource_6"],
#     ["400", "user_7", "resource_2"],
#     ["100", "user_8", "resource_2"],
#     ["54359", "user_1", "resource_3"],
# ]


# We would like to compute user sessions, specifically: write a function that takes the logs and returns a data structure that associates to each user their earliest and latest access times.

# Example:
# {'user_1': [54001, 58523],
#  'user_2': [54060, 62314],
#  'user_3': [53941, 53941],
#  'user_4': [58522, 58522],
#  'user_5': [53651, 53651],
#  'user_6': [2, 215],
#  'user_7': [400, 400],
#  'user_8': [100, 100]}
'''

def Indeed(logs):

    user_dict = {}

    for lst in logs:
        user = lst[1]
        timestamp = lst[0]
        if user in user_dict.keys():
            user_dict[user].append(timestamp)
        else:
            user_dict[user] = []
            user_dict[user].append(timestamp)

    for key, val in user_dict.items():
        temp_lst = sorted(val)
        user_list = []
        user_list.append(temp_lst[0])
        user_list.append(temp_lst[-1])
        user_dict[key] = user_list
    return sorted(user_dict.items(), key=lambda x: x[0])

def main():

    logs = [
        ["58523", "user_1", "resource_1"],
        ["62314", "user_2", "resource_2"],
        ["54001", "user_1", "resource_3"],
        ["215", "user_6", "resource_4"],
        ["200", "user_6", "resource_5"],
        ["54060", "user_2", "resource_3"],
        ["53941", "user_3", "resource_3"],
        ["58522", "user_4", "resource_1"],
        ["53651", "user_5", "resource_3"],
        ["2", "user_6", "resource_1"],
        ["100", "user_6", "resource_6"],
        ["400", "user_7", "resource_2"],
        ["100", "user_8", "resource_2"],
        ["54359", "user_1", "resource_3"]]
    print(Indeed(logs))

if __name__=='__main__':
    main()