# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# https://leetcode-cn.com/problems/merge-sorted-array/


class Solution1:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Python 列表内置方法
        """
        nums1[:] = sorted(nums1[:m] + nums2)


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    s1 = Solution1()
    s1.merge(nums1, m, nums2, n)
    print(nums1)



