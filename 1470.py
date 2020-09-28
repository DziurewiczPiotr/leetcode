from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        _ = []
        [(_.append(nums[i]), _.append(nums[i + n])) for i in range(n)]
        return _

print(Solution().shuffle([2,5,1,3,4,7], 3))