class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen_dict:
                return [seen_dict[comp], i]
            seen_dict[nums[i]] = i

        return []
