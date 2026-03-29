class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        def build(start, end):
            if start > end: return [None]
            res = []
            for i in range(start, end + 1):
                for l in build(start, i - 1):
                    for r in build(i + 1, end):
                        res.append(TreeNode(i, l, r))
            return res
        return build(1, n) if n else []

