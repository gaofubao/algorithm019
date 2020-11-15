# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# https://leetcode-cn.com/problems/trapping-rain-water/


class Solution1:
    """
    单调栈
    """
    def trap(self, height) -> int:
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res


if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    
    s1 = Solution1()
    result = s1.trap(height)
    print(result)

