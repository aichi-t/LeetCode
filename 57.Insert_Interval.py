def insertInterval(intervals, newInterval):
    """
    Time Complexity: O(NlogN). Utilized mergeInterval solution.
    """
    intervals.append(newInterval)
    return mergeInterval(intervals)


def insertInterval2(intervals, newInterval):
    """
    Time Complexity: O(N). Utilized the fact that the intervals are sorted
    """

    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    pass


def mergeInterval(intervals):
    result = []
    for item in sorted(intervals, key=lambda item: item[0]):
        if result and item[0] <= result[-1][-1]:
            result[-1][-1] = max(result[-1][-1], item[-1])
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    # intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    # intervals = [[1, 3], [2, 5], [6, 9]]
    # print(mergeInterval(intervals))

    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    # print(insertInterval(intervals, newInterval))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insertInterval(intervals, newInterval))

    intervals = [[1, 5]]
    newInterval = [2, 7]
    print(insertInterval(intervals, newInterval))

    b = [[1, 2]]
    for i, item in enumerate(b):
        print(item.start)
