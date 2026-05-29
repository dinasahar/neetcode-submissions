class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while len(nums)>1:
            elem = nums[0]
            nums.remove(nums[0])
            # print(nums)
            if elem in nums:
                return True
        else: 
             return False
