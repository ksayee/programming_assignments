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
#Q2
# Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.

# Example:
# ('resource_3', 3)
'''


def GetWindowCount(i, sort_list):
    window = 300
    cnt = 0
    for j in range(i, len(sort_list)):
        diff = sort_list[i] - sort_list[i - 1]
        if diff < window:
            window = window - diff
            cnt = cnt + 1
        else:
            break
    return cnt

def Indeed(logs):
    resource_dict = {}

    for lst in logs:
        resource = lst[2]
        timestamp = lst[0]
        if resource in resource_dict.keys():
            resource_dict[resource].append(int(timestamp))
        else:
            resource_dict[resource] = []
            resource_dict[resource].append(int(timestamp))

    final_dict = {}
    for key, val in resource_dict.items():
        sort_list = sorted(val)
        for i in range(1, len(sort_list)):
            count = GetWindowCount(i, sort_list)
            if key in final_dict.keys():
                final_dict[key].append(count)
            else:
                final_dict[key] = []
                final_dict[key].append(count)
    max = 0
    max_key = ''

    for key, val in final_dict.items():
        if sorted(val, reverse=True)[0] > max:
            max = sorted(val, reverse=True)[0]
            max_key = key
    tup = (max_key, max)
    return tup

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