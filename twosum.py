from typing import List, Union

list_of_numbers = [9,4,6,12,5,1,0]

def twoSum(nums: List[int], target: int)-> Union[str | List[int]]:
    ##brute force way
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    ##optimized way
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

    return "no combination found"

result = twoSum(list_of_numbers, int(input("choose a target value : ")))

print(result)