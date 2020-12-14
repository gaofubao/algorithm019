# 给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。
# 学生出勤记录是只包含以下三个字符的字符串：
# 'A' : Absent，缺勤
# 'L' : Late，迟到
# 'P' : Present，到场
# 如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。

# https://leetcode-cn.com/problems/student-attendance-record-ii

class Solution:
    def checkRecord(self, n: int) -> int:
        pass