class Solution:
    def total_mul(self, nums: List[int]) -> int:
        total = 1
        for num in nums:
            total *= num
        return total

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            new_nums = nums[:]      # Make a copy
            del new_nums[i]         # Remove element at index i
            output.append(self.total_mul(new_nums))

        return output