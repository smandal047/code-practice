from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        l = len(nums)
        s = len(set(nums))

        if l == s:
            return False
        else:
            return True