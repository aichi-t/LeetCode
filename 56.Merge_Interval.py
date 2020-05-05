def merge(intervals):

    # Loop through intervals
    # After merge, change the current list to the merged list
    if len(intervals) < 2:
        return intervals
    result = []
    curr_list = intervals[0]
    for i in range(1, len(intervals)):
        next_list = intervals[i]
        if curr_list[-1] >= next_list[0] and next_list[-1] >= curr_list[0]:
            curr_list[-1] = max(next_list[-1], curr_list[-1])
            curr_list[0] = min(next_list[0], curr_list[0])
        else:
            result.append(curr_list)
            curr_list = next_list
        if i == len(intervals) - 1:
            result.append(curr_list)
    return result


def merge2(intervals):
    result = []
    for item in sorted(intervals, key=lambda i: i[0]):
        if result and item[0] <= result[-1][-1]:
            result[-1][-1] = max(result[-1][-1], item[-1])
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [0, 0]]
    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    # intervals = [[1, 3], [2, 6], [8, 10], [10, 18]]
    # intervals = [[1, 4], [0, 4]]
    # intervals = [[1, 3], [5, 6]]
    # print(merge(intervals))
    intervals.sort(key=lambda intervals: intervals[0])
    print(intervals)
    print(merge(intervals))
    print(merge2(intervals))
