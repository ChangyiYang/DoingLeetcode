# https://leetcode.cn/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import random

    # a variation of quick sort
        def quick_sort_k(arr, k):

            if len(arr) == 1:
                return arr[0]
            
            if len(arr) == 0:
                return -1

            pivot_index = random.randint(0, len(arr) - 1)  # 选择随机位置作为基准元素的索引
            pivot = arr[pivot_index]
            arr[0], arr[pivot_index] = arr[pivot_index], arr[0]  # 将基准元素与数组的第一个元素交换位置
            left = [x for x in arr[1:] if x < pivot]
            right = [x for x in arr[1:] if x >= pivot]

            print('pivot',pivot)

            if len(left) == k-1:
                return pivot
            
            if len(left) > k-1:
                return quick_sort_k(left, k)
            
            else:
                return quick_sort_k(right, k - (len(left)+1))

        return quick_sort_k(nums, len(nums) - k+1)


x = Solution()

nums = [3,2,1,5,6,4]
k =2
print(x.findKthLargest(nums, k))
