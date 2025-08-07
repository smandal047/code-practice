from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h_map = {}

        for i, no in enumerate(nums):
            diff = target - no

            if diff in h_map:
                return [h_map[diff], i]
            else:
                h_map[no] = i
        
        return []