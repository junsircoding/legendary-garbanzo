class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # 哈希表
        # dict1, dict2 = dict(), dict()
        # for elem in s:
        #     if elem in dict1:
        #         dict1[elem] += 1
        #     else:
        #         dict1[elem] = 1

        # for elem in t:
        #     if elem in dict2:
        #         dict2[elem] += 1
        #     else:
        #         dict2[elem] = 1

        # return dict1 == dict2

        # 哈希表简化
        # dict1, dict2 = dict(), dict()
        # for elem in s:
        #     dict1[elem] = dict1.get(elem, 0) + 1
        # for elem in t:
        #     dict2[elem] = dict2.get(elem, 0) + 1
        # return dict1 == dict2

        # 数组用 ASCII 十进制数作 index
        dict1, dict2 = [0]*26, [0]*26
        for elem in s:
            dict1[ord(elem) - ord("a")] += 1
        for elem in t:
            dict2[ord(elem) - ord("a")] += 1
        return dict1 == dict2

