# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution1:
    """
    递归法
    """
    def preorderTraversal(self, root):
        if not root:
            return None

        print(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

class Solution2:
    """
    递归法
    """
    def preorderTraversal(self, root):
        def preorder(root):
            if not root: return None

            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = []
        preorder(root)
        return res

class Solution3:
    """
    迭代法
    """
    def preorderTraversal(self, root):
        res = list()
        if not root:
            return None

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res



if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g


    s1 = Solution2()
    result = s1.preorderTraversal(a)
    print(result)

