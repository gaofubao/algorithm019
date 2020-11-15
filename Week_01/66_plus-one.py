# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# https://leetcode-cn.com/problems/plus-one/



class Solution1:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i]:
                return digits

        digits = [0 for _ in range(len(digits) + 1)]
        digits[0] = 1
        return digits


if __name__ == "__main__":
    digits = [1,2,3]

    s1 = Solution1()
    result = s1.plusOne(digits)
    print(result)
