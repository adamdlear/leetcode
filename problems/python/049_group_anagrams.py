from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            chars = sorted(s)
            sorted_s = "".join(chars)

            if sorted_s not in anagrams:
                anagrams[sorted_s] = [s]
            else:
                group = anagrams[sorted_s]
                group.append(s)
                anagrams[sorted_s] = group

        return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    print(res)
