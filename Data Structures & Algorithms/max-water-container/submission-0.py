class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res =0

        while l<r:
            area = min(heights[l], heights[r])*(r-l)
            res = max(area,res)
            if heights[l]<heights[r]:
                l += 1
            elif heights[l] == heights[r]:
                if heights[l+1] > heights[r-1]:
                    l +=1
                else:
                    r -=1
            else:
                r -=1
        return res


        

        