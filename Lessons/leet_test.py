import math
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            if target - i in nums[nums.index(i) + 1::]:
                first_index = nums.index(i)
                second_index = nums.index(target - i)

                if first_index == second_index:
                    nums.remove(i)
                    second_index = nums.index(i) + 1

                return [
                    first_index,
                    second_index
                ]


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(list(s)) == len(set(s)):
            return len(s)
        results = []
        counter = 0
        for i in range(len(s)):
            pbr = s[counter::]  # possible best result
            this_pbr_seq = ""
            for _ in pbr:
                print(pbr, _)
                if _ not in this_pbr_seq:
                    this_pbr_seq += _
                else:
                    print(this_pbr_seq)
                    if this_pbr_seq in s:
                        results.append(this_pbr_seq)
                        counter += 1
        print(results)
        if len(results):
            return max([len(i) for i in results])
        return 0


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        merged_list_of_nums = nums1 + nums2
        merged_list_of_nums.sort()
        list_len = len(merged_list_of_nums)
        print(merged_list_of_nums, list_len)

        if list_len % 2 == 0:
            print("list_len % 2")
            first_index = int(list_len / 2) - 1
            second_index = int(list_len / 2)
            first_num = merged_list_of_nums[first_index]
            second_num = merged_list_of_nums[second_index]
            return (first_num + second_num) / 2

        return float(merged_list_of_nums[
                         int(math.floor(list_len / 2))
                     ])


sol = Solution()
print(sol.findMedianSortedArrays([-1, -2, -3], [1, 2]))  # 12
