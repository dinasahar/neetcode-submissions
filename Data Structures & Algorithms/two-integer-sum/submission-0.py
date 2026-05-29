class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums
        for i in range(0, len(nums)):
            for j in range(0, len(nums_copy)):
                if nums[i]+nums_copy[j] == target and i!=j:
                    return [i,j]
