# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
# https://leetcode-cn.com/problems/top-k-frequent-elements/


import collections
class Solution1:
    """
    哈希表
    """
    def topKFrequent(self, nums, k):
        if k >= len(nums):
            return nums

        # 将数组元素映射到哈希表中
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1

        # dict按值排序
        d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

        # 取Top K
        res = []
        for t in d_sorted[:k]:
            res.append(t[0])
        return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    s1= Solution1()
    result = s1.topKFrequent(nums, k)
    print(result)




