from typing import List
class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:
#     # 暴力破解 N^3
#         result = list()
#         nums.sort()
#         print(nums)
#         for idx1 in range(0, len(nums)-2):
#             for idx2 in range(idx1+1, len(nums)-1):
#                 for idx3 in range(idx2+1, len(nums)):
#                     choice = nums[idx1] + nums[idx2] + nums[idx3]
#                     if choice == 0:
#                         aa = sorted([nums[idx1], nums[idx2], nums[idx3]])
#                         if aa not in result:
#                             result.append(aa)
# 
#         return result
# 
#         result = list()
#         nums.sort()
# 
#         for idx1 in range(0, len(nums)-2):
#             for idx2 in range(idx1+1, len(nums)-1):
#                 elem1 = nums[idx1]
#                 elem2 = nums[idx2]
#                 elem3 = -elem1-elem2
#                 nums_rest = nums[0:idx1]+nums[idx1+1:idx2]+nums[idx2+1:]
#                 if elem3 in nums_rest: 
#                     aa = sorted([elem1, elem2, elem3])
#                     if aa not in result:
#                         result.append(aa)
# 
#         return result
# 
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i>= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))

test_nums = [[1, 2, -2, -1],
             [0,0,0],

             ]
test_answer = [[],[[0,0,0]]]
s = Solution()
for q,a in zip(test_nums, test_answer):
    result = s.threeSum(q)
    print(result == a)
    print(result)
    print(a)
                

