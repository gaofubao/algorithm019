# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# https://leetcode-cn.com/problems/move-zeroes/


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Python列表的内置方法
        """
        for i in nums[:]:
            if i == 0:
                nums.remove(i)
                nums.append(0)


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        双指针法
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]

    s1 = Solution2()
    s1.moveZeroes(nums)
    print(nums)
