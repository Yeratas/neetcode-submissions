class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i  in range(len(nums)):
            difference = 0
            difference = target - nums[i]
            if difference not in hash_table:
                hash_table[nums[i]] = i
            else:
                return [hash_table[difference],i]
            