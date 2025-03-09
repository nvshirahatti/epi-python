def insertion_sort(nums):
    for i in range(0, len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums
if __name__ == "__main__":
    nums = [1, 3, 2, 5, 4, 0, 9]
    print(insertion_sort(nums))