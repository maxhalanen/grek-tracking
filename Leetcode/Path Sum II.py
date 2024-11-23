# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []

        def trav(root, comb, target):
            print(comb, target)

            if not root:
                return

            if not root.left and not root.right and target + root.val == targetSum:
                comb.append(root.val)
                ans.append(list(comb))
                comb.pop()
                return

            comb.append(root.val)
            trav(root.left, comb, target + root.val)
            trav(root.right, comb, target + root.val)
            comb.pop()
            

        
        trav(root, [], 0)

        return ans
            
