Problem #1: Insert into a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
       
        temp = root
        while True:
            if val > temp.val:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                temp = temp.right    
            else:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                temp = temp.left




Problem #2: Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative solution:
        counter = 0
        stack = []
        cur = root


        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left


            cur = stack.pop()
            counter += 1
            if counter == k:
                return cur.val
            cur = cur.right        


      
# recursive inorder traversal:
        # self.counter = 1
        # self.smallest = None


        # def inorder(node):
        #     if not node:
        #         return
           
        #     inorder(node.left)
        #     if self.counter == k:
        #         self.smallest = node.val    
        #     self.counter += 1
        #     inorder(node.right)


        # inorder(root)
        # return self.smallest  




Problem #3: Validate Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node, left, right):
            if not node:
                return True
               
            if not node.val < right or not node.val > left:
                return False


            return (dfs(node.left,left,node.val) and dfs(node.right,node.val,right))


        return dfs(root,float('-inf'),float('inf'))    



(Bonus) Problem #4: Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None


        root = TreeNode(preorder[0])
        midpoint = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:midpoint + 1], inorder[:midpoint])
        root.right = self.buildTree(preorder[midpoint + 1 :], inorder[midpoint + 1 :])
        return root
       



(Bonus) Problem #5: Binary Tree Pruning
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)


            if root.val == 0 and root.left == None and root.right == None:
                return None


        return root    
       




           
       
    


