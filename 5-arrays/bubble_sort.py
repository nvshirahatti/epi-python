def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

if __name__ == "__main__":
    nums = [1, 10, 2, 5, 4, 9, 8, 7, 6, 3]
    print(bubble_sort(nums))
    nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10]
    print(bubble_sort(nums)[::-1])
