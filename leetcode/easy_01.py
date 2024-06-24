class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1.
        for num1 in nums:
            if num1 > target: (not exist)
                continue
            elif num1 == target: (not exist)
                return [num1.idx]
            else:
                num2 = target - num1
                idx1 = nums.index(num1)
                if num1 == num2:
                    if num2 in nums[idx1+1:]:
                        return [idx1, nums[idx1+1:].index(num2)+idx1+1]
                else:
                    if num2 in nums:
                        idx2 = nums.index(num2)
                            return [idx1, nums.index(num2)]

        2.
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map[target - x]]
            hash_map[x] = i
        """
        for num1 in nums:
            num2 = target - num1
            idx1 = nums.index(num1)
            if num1 == num2:
                if num2 in nums[idx1+1:]:
                    return [idx1, nums[idx1+1:].index(num2)+idx1+1]
            else:
                if num2 in nums:
                    idx2 = nums.index(num2)
                    return [idx1, nums.index(num2)]
