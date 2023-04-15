# https://leetcode.cn/problems/uncrossed-lines/

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        # 使用动态规划， D[i][j] 代表 nums1 前i个 和 nums2 前j个 最多线数

        D = [[0 for j in range(len(nums2)+1)] for i in range(len(nums1)+1)]


        D[0][0] = 0

        for i in range(len(nums1)):
            D[i][0] = 0

        for j in range(len(nums2)):
            D[0][j] = 0


        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    D[i+1][j+1] = D[i][j] + 1
                
                else:
                    D[i+1][j+1] = max(D[i][j+1], D[i+1][j])

        return D[len(nums1)][len(nums2)]