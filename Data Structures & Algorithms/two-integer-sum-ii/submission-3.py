class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        output = [ ]
        while numbers[left]+numbers[right] != target:
            if numbers[left]+numbers[right]>target:
                right = right-1

            if numbers[left]+numbers[right]<target:
                left = left + 1
        output.append(left+1)
        output.append(right+1)
        return output
        