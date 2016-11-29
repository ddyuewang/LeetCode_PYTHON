### Lowest Common Ancestor of a Binary Search Tree
def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if (root.val - p.val) * (root.val - q.val) <= 0:
        return root
    elif p.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return self.lowestCommonAncestor(root.right, p, q)

### Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # 发现目标结点，则标记（left或right）
    if (root == None or root == p or root == q):
        return root;
    # 查看左右子树是否有目标结点
    left = self.lowestCommonAncestor(root.left, p, q);
    right = self.lowestCommonAncestor(root.right, p, q);
    # 左右子树同时含有目标结点，则该结点是lca
    if (left != None and right != None):
        return root;
    # 左右子树只有一个含有目标结点，向上返回
    if left == None:
        return right
    else:
        return left