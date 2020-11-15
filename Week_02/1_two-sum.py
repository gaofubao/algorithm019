# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# https://leetcode-cn.com/problems/two-sum/



class Solution1:
    """
    暴力枚举
    """
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    """
    哈希表
    """
    def twoSum(self, nums, target):
        hashtable = {}
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


if __name__ == "__main__":
    nums = [4, 4, 11, 15]
    target = 8

    s1 = Solution2()
    result = s1.twoSum(nums, target)
    print(result)

