# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# https://leetcode-cn.com/problems/rotate-array/


class Solution1:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        反转数组
        """
        length = len(nums)
        k = k % length

        self.reverse(nums, 0, length-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)

    def reverse(self, nums, start, end):
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3

    s1 = Solution1()
    s1.rotate(nums, k)
    print(nums)