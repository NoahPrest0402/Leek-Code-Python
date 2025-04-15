class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_list = {}
        for i, num in enumerate(nums):
            target_num = target - num
            if target_num in num_list:
                return [num_list[target_num], i]
            num_list[num] = i