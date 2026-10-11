class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in numbers:
                return [numbers[needed], i]
            numbers[num] = i