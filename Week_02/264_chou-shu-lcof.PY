# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
# https://leetcode-cn.com/problems/chou-shu-lcof/
# https://leetcode-cn.com/problems/ugly-number-ii/

from heapq import heappop, heappush
class Ugly:
    def __init__(self):
        # 使用哈希表去重
        seen = {1, }
        # 用于存储 Ugly Number
        self.nums = []
        # 初始化堆
        heap = []
        heappush(heap, 1)
        for _ in range(1699):
            # 从堆中取出最小的元素
            curr_ugly = heappop(heap)
            self.nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)

class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        u = Ugly()
        return u.nums[n-1]          


if __name__ == "__main__":
    n = 10

    s1 = Solution1()
    result = s1.nthUglyNumber(n)
    print(result)

