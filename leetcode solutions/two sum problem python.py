def two_sum(nums, target):
    # Create a hash map to store the difference and index of each element
    hash_map = {}
    for i in range(len(nums)):
        num = nums[i]
        diff = target - num
        if diff in hash_map:
            # If the difference exists in the hash map, return the indices
            return [hash_map[diff], i]
        else:
            # Otherwise, add the current element to the hash map
            hash_map[num] = i
    # If no solution is found, return an empty list
    return []
nums = [2, 7, 11, 15]
target = 18
print(two_sum(nums, target))  # Output: [0, 1]
