from typing import List


class Solution:
    def twoSum(self, nums, target) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap.keys():
                return [hashmap[diff], index]
            else:
                hashmap[value] = index


result = Solution()
nums = [10, 2, 60, 40, 6]
target = 100
print(result.twoSum(nums, target))
print(result.twoSum2(nums, target))

# Reference
# https://www.code-recipe.com/post/two-sum
