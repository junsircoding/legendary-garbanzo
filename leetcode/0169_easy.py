class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 暴力
        # Map
        map_count = dict()
        max_val, max_count = "", 0

        for elem in nums:
            map_count[elem] = map_count.get(elem, 0) + 1
            if map_count[elem] > max_count:
                max_count = map_count[elem]
                max_val = elem

        return max_val

