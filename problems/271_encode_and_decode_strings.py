from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""

        for s in strs:
            e += str(len(s))
            e += "#"
            e += s

        return e

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            dist = int(s[i:j])
            start = j + 1
            end = start + dist
            res.append(s[start:end])

            i = end

        return res


if __name__ == "__main__":
    # strs = [""]
    strs = ["Hello", "World"]
    # strs = ["we", "say", ":", "yes", "!@#$%^&*()"]
    e = Solution().encode(strs)
    print(e)
    d = Solution().decode(e)
    print(d)
