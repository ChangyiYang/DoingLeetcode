# https://leetcode.cn/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:


        # DP 
        n = len(nums)

        D = [0] * n

        # D[i] means the longest increasing subsequence ends at i 
        for i in range(n):
            

