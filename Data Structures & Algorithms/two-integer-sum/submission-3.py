class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_indices ={}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_indices:
                return [prev_indices[diff], i]
            prev_indices[n] = i
        
        return []


        
        

            

        