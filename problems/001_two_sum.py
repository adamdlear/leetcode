from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1 = -1
        i2 = -1

        seen = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                i1 = i
                i2 = seen[diff]

            seen[num] = i

        return [i1, i2]
