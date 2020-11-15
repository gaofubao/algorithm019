# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# https://leetcode-cn.com/problems/group-anagrams/

import collections
class Solution1:
    """
    哈希表
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = collections.defaultdict(list)
        for s in strs:
            dd[tuple(sorted(s))].append(s)
        return list(dd.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    s1 = Solution1()
    result = s1.groupAnagrams(strs)
    print(result)


