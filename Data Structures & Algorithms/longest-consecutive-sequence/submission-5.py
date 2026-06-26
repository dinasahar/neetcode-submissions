class Solution:
    def counting_sort(self, arr):
        if not arr:
            return arr
            
        max_val = max(arr)
        min_val = min(arr)
        range_of_elements = max_val - min_val + 1
        
        count_arr = [0] * range_of_elements
        output_arr = [0] * len(arr)
        
        for num in arr:
            count_arr[num - min_val] += 1
            
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]
            
        for num in reversed(arr):
            output_arr[count_arr[num - min_val] - 1] = num
            count_arr[num - min_val] -= 1
            
        return output_arr

    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = self.counting_sort(nums)

        if len(sorted_list) == 0:
            return 0

        current = 1
        longest = 1

        for i in range(0, len(sorted_list) - 1):
            if sorted_list[i + 1] == sorted_list[i]:
                continue

            elif sorted_list[i + 1] == sorted_list[i] + 1:
                current += 1
                longest = max(longest, current)

            else:
                current = 1

        return longest