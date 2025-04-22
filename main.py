# Global counters
recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    global recursions, comparisons

    if lower > upper:
        return -1

    recursions += 1
    mid = (lower + upper) // 2

    comparisons += 1
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        comparisons += 1
        return binary_search(nums, target, mid + 1, upper)
    else:
        comparisons += 1
        return binary_search(nums, target, lower, mid - 1)

if __name__ == '__main__':
    nums = [int(n) for n in input().split()]
    target = int(input())
    index = binary_search(nums, target, 0, len(nums) - 1)
    # Final output with no extra spacing or blank lines
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
