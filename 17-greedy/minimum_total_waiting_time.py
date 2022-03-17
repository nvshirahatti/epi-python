# O(nlogn) time, O(1) space
def minimum_total_waiting_time(service_times):
    service_times.sort()
    total_wait_time = 0

    for i, service_time in enumerate(service_times):
        number_remain_queries = len(service_times) - i - 1
        total_wait_time += service_time * number_remain_queries

    return total_wait_time


if __name__ == "__main__":
    service_times = [2, 5, 1, 3]
    assert minimum_total_waiting_time(service_times) == 10
    print("All tests passed!")
