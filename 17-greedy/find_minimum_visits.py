# O(nlogn) time, O(1) space
def find_minimum_visits(intervals):
    # [0, 3]
    # [2, 6] -> [2, 3]
    # [3, 4] -> 3
    # [6, 9] -> 6
    intervals.sort(key=lambda interval: interval[0])
    current = []
    res = []

    for interval in intervals:
        if not current:
            current = interval
            continue
        current = [max(current[0], interval[0]), min(current[1], interval[1])]
        if current[0] == current[1]:
            res.append(current[0])
            current = []

    if current:
        res.append(current[0])

    return res


# O(nlogn) time, O(1) space
def find_minimum_visits_2(intervals):
    # sort intervals by endpoints
    intervals.sort(key=lambda interval: interval[1])
    # [0, 3], [3, 4], [2, 6], [6, 9]
    last_visit_time = float("-inf")
    res = []
    for interval in intervals:
        if interval[0] > last_visit_time:
            last_visit_time = interval[1]
            res.append(last_visit_time)
    return res


if __name__ == "__main__":
    intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]
    assert find_minimum_visits(intervals) == [3, 6]
    assert find_minimum_visits_2(intervals) == [3, 9]
    print("All tests passed!")
