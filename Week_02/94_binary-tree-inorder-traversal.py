# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/


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
    def inorderTraversal(self, root):
        def inorder(root):
            if not root: return None

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
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


    s1 = Solution1()
    result = s1.inorderTraversal(a)
    print(result)

