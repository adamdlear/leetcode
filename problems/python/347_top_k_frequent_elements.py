import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Example 3:
        Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
        Output: [1,2]
        """
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        sorted_counts = dict(
            sorted(counts.items(), key=lambda item: item[1], reverse=True)
        )

        return list(sorted_counts.keys())[:k]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = Solution().topKFrequent(nums, k)
    print(result)
