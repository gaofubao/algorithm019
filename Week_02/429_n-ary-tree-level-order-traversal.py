# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    """
    没有想明白，以及如何进行验证
    """
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result




if __name__ == "__main__":
    pass




