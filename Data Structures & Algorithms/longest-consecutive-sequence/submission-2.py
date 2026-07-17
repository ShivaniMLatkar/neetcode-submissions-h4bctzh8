class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Check if it is the start of a sequence
            if (num - 1) not in numSet:
                length = 1
                # Keep tracking the length of the consecutive sequence
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest