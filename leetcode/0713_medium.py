# -*- coding: utf-8 -*-

"""
暴力破解的方法是遍历所有的 subarray, 然后算出它们的乘积, 筛选出小于 k 的数量
这样做的时间复杂度是 O(n^2), 数据量大的时候, 根本没法用, 必须使用更高效的方法

方案1, 滑动窗口模式
当问题需要使用子数组实现目标并且无法独立选择单个元素时，可以使用此模式。

滑动窗口模式背后的概念是通过添加元素并计算其乘积来维护一个从右侧不断扩展的窗口，直到满足条件。 
一旦条件满足，我们通过从左侧缩小窗口来调整窗口，直到再次满足条件。

当我们在数组上滑动窗口时，我们的目标是识别 nums 数组中元素乘积小于 k 的所有子数组。 
对于每个右侧位置，如果窗口从左到右的元素的乘积小于 k，则添加右侧的元素会生成乘积小于 k 的新子数组。

此类子数组的计数由 right - left + 1 的差值确定，该差表示以右侧结束并以右侧和左侧（含）之间的任何元素开始的子数组的数量。 
本质上，此计数包含仅由当前元素本身组成的子数组，以及延伸回窗口左边界（左）的所有可能的子数组。

考虑一个包含元素 3、4 和 5 的示例窗口。如果我们在窗口中包含 6，则需要计算以 6 结尾的所有可能的子数组。
这些子数组可以通过从当前窗口内的任何元素开始并扩展到 6. 因此，子数组将是：

    - [6] (subarray consisting only of 6)
    - [5, 6] (subarray starting from 5 and ending at 6)
    - [4, 5, 6] (subarray starting from 4 and ending at 6)
    - [3, 4, 5, 6] (subarray starting from 3 and ending at 6)

通过计算 right - left + 1，我们枚举以窗口当前元素 (nums[right]) 结尾的所有子数组。 
这确保了当我们在数组上滑动窗口时计算所有可能的子数组。 
正如我们所观察到的，将元素 6 添加到窗口中创建了 4 个新的子数组。

关键的见解是，一旦乘积变得小于 k，通过选择当前窗口（从左到右）内的元素子集形成的所有可能的子数组也将具有严格小于 k 的乘积。

因此，只要乘积有效，我们就会将当前窗口大小（右 - 左 + 1）添加到子数组的总数中。

算法
检查 k 是否小于或等于 1。在这种情况下，任何子数组的乘积都不能小于 k，因此返回 0。
将变量totalCount初始化为0，以存储乘积小于k的子数组的最终计数，并将product初始化为1，表示窗口内元素的乘积（最初为空）。
使用左右两个指针来定义滑动窗口。 使用 for 循环遍历 nums 数组，直到 right 到达末尾。
在循环内，将当前乘积乘以右指针 (nums[right]) 处的元素。 这有效地将新元素包含在窗口中。
当当前乘积大于或等于k时，窗口需要缩小以排除使乘积超过k的元素。
将乘积除以左指针 (nums[left]) 处的元素。
左加 1 可将窗口向右移动一位，从而有效排除最左边的元素。
通过将有效子数组的数量与当前窗口大小（右 - 左 + 1）相加来更新 TotalCount。
返回总计数。

太难了，看不懂。

"""

from typing import List

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         result = 0
#         # window size is 0
#         # result += len(list(filter(lambda x: x<k, nums)))
#         # print(0, result)
#         # window size is > 1
#         for W_SIZE in range(0, len(nums)):
#             # W_SIZE = 1
#             for right in range(len(nums) - 1, -1, -1):
#                 left = right - W_SIZE
#                 if left < 0:
#                     break
#                 product = 1
#                 # print(f"nums[{left}], {nums[left]}", f"nums[{right}], {nums[right]}")
#                 for i in range(left, right+1):
#                     product *= nums[i]
#                     # print(nums[i], end=",")
#                 # print()
#                 # print(product)
#                 if product < k:
#                     result += 1


#         # window size is 2
#         # ...
#         # window size is len(nums) - 1
#         return result

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Handle edge cases where k is 0 or 1 (no subarrays possible)
        if k <= 1:
            return 0

        total_count = 0
        product = 1

        # Use two pointers to maintain a sliding window
        left = 0
        for right, num in enumerate(nums):
            product *= num  # Expand the window by including the element at the right pointer

            # Shrink the window from the left while the product is greater than or equal to k
            while product >= k:
                product //= nums[left]  # Remove the element at the left pointer from the product
                left += 1

            # Update the total count by adding the number of valid subarrays with the current window size
            total_count += right - left + 1  # right - left + 1 represents the current window size

        return total_count


s = Solution()
print(s.numSubarrayProductLessThanK([1, 1, 1], 2))
