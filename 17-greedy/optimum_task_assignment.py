# O(nlogn) time, O(n) space
def optimum_task_assingment(task_durations):
    n = len(task_durations)
    task_durations.sort()
    # tilde operator https://stackoverflow.com/questions/8305199/the-tilde-operator-in-python
    return [(task_durations[i], task_durations[~i]) for i in range(n // 2)]


if __name__ == "__main__":
    task_durations = [5, 2, 1, 6, 4, 4]
    assert optimum_task_assingment(task_durations) == [(1, 6), (2, 5), (4, 4)]
    print("All tests passed!")
