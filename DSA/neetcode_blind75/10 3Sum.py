from typing import List

# solved using 2 pointer algo
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sort_nums = sorted(nums)
        len_nums = len(nums)
        three_sums = []

        for index in range(len_nums):

            # init index duplicate handling
            if index > 0 and sort_nums[index] == sort_nums[index-1]:
                continue

            left = index+1
            right = len_nums-1

            while left < right:

                total = sort_nums[index] + sort_nums[left] + sort_nums[right]

                # handles the action when total is achieved
                if total == 0:
                    three_sums.append([sort_nums[index], sort_nums[left], sort_nums[right]])

                    # duplicate handling for left right indexes
                    while left < right and sort_nums[left] == sort_nums[left+1]:
                        left+=1
                    while left < right and sort_nums[right] == sort_nums[right-1]:
                        right-=1

                # handles the pointers irrespective of total
                if total < 0:
                    left += 1
                else:
                    right -= 1
        
        return three_sums


if __name__ == '__main__':

    print(
        Solution.threeSum(None, nums=[-1,0,1,2,-1,-4])
    )
