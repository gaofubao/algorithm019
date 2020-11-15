# 给定一个 N 叉树，返回其节点值的前序遍历。
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution1:
    """
    没有想明白，以及如何进行验证
    """
    def preorder(self, root: 'Node'):
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
                
        return output


if __name__ == "__main__":
    pass


