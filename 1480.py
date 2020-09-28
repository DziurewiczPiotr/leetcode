from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final_nums = [sum(nums[:i + 1]) for i in range(len(nums))]
        return(final_nums)


print(Solution().runningSum([3,1,2,10,1]))