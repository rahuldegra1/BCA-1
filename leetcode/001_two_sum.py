
def twoSum(nums, target):
    history = {}
    for index, num in enumerate(nums):
        needed = target - num
        if needed in history:
            return [history[needed], index]
        history[num] = index
        
print(twoSum([2, 7, 11, 15], 9)) # Expected: [0, 1]
print(twoSum([3, 2, 4], 6))      # Expected: [1, 2]
print(twoSum([3, 3], 6))         # Expected: [0, 1]