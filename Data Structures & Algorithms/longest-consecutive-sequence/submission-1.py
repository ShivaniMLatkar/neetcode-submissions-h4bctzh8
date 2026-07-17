class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        res = 1
        n=len(nums)
        l = 0

        for r in range(1, n):
            if nums[r] == nums[r - 1]:
                l += 1

            elif nums[r] != nums[r-1]+1:
                res = max(r-l, res)
                l = r
        
        return max(n - l, res)
            
            