# https://leetcode.cn/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 学过，利用recurrion和分而治之


        # this will return the max subarray exists in list nums
        def maxSubArrayRecur(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 0 :
                return 0

            k = len(nums)//2

            left = nums[:k]
            right = nums[k:]

            # consider the condition when the max sub array cross the split line

            # calculate the max sub array in left such that the end of it is k

            max_left = left[-1]

            count = 0
            for i in range(1,len(left)+1):

                count += left[-i]

                max_left = max(max_left, count)

            count = 0
            max_right = right[0]
            for j in range(len(right)):
                count += right[j]
                max_right = max(max_right, count)

            middle = max_left + max_right



            return max(maxSubArrayRecur(left), maxSubArrayRecur(right), middle)

        return maxSubArrayRecur(nums)
