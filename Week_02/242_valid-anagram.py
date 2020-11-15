# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词（字母异位词指字母相同，但排列不同的字符串）
# https://leetcode-cn.com/problems/valid-anagram/description/


class Solution1:
    """
    暴力法-排序
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if s.__len__() != t.__len__():
            return False

        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()

        if s_list == t_list:
            return True

        return False


import collections
class Solution2:
    """
    哈希表
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


class Solution3:
    """
    哈希表
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alpha = [0 for _ in range(26)]
        for i in range(len(s)):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1

        return not any(alpha)

# any(iterable) Return True if any element of the iterable is true. If the iterable is empty, return False. 
# all(iterable) Return True if all elements of the iterable are true (or if the iterable is empty).



if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"

    s1 = Solution3()
    result = s1.isAnagram(s, t)
    print(result)




