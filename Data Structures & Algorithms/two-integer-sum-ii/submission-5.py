class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1

        while l <= r:

            my_sum = numbers[l] + numbers[r]

            if my_sum == target:
                return [l+1, r+1]

            elif my_sum < target:
                while l == l+1:
                    l+=1
                l+=1

            elif my_sum > target:
                while r == r-1:
                    r-=1
                r-=1


        