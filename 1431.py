from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if i + extraCandies >= max(candies) else False for i in candies]

print(Solution().kidsWithCandies([4,2,1,1,2], 1))
