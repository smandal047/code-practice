from typing import List

class Solution:

    # brute force method - exhausts execution time
    def maxArea1(self, height: List[int]) -> int:
        
        area = 0
        len_cols = len(height)

        for index, col in enumerate(height):

            left = index+1
            dist = 1

            while left < len_cols:
                
                adj_col = min(col, height[left])
                area = max(area, adj_col*dist)
                    
                left+=1
                dist+=1
        
        return area
    
    # works but uses 1 extra min fx
    def maxArea2(self, height: List[int]) -> int:

        area = 0
        left_index = 0
        right_index = len(height)-1

        while left_index < right_index:

            new_area = min(height[left_index], height[right_index]) * (right_index - left_index)
            area = max(area, new_area)

            if height[left_index] < height[right_index]:
                left_index+=1
            else:
                right_index-=1
        
        return area
    
    # optimised two pointer algo
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        left_index = 0
        right_index = len(height)-1

        while left_index < right_index:

            # new_area = min(height[left_index], height[right_index]) * (right_index - left_index)
            # area = max(area, new_area)

            if height[left_index] < height[right_index]:
                area = max(
                    area,
                    height[left_index] * (right_index - left_index)
                )
                left_index+=1
            else:
                area = max(
                    area,
                    height[right_index] * (right_index - left_index)
                )
                right_index-=1
        
        return area



if __name__ == '__main__':

    print(
        Solution.maxArea(None, [1,8,6,2,5,4,8,3,7])
    )

    print(
        Solution.maxArea(None, [1,1,3])
    )
