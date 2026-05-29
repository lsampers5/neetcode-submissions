class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:

            area = (right - left) * min(heights[right], heights[left])
            result = max(result, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return result


            
            
             


