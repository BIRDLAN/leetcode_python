#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#


# @lc code=start
#  Time: O(n), space: O(nlogn), n = length of nums
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        for index, num in enumerate(nums):
            key = dic.get(target - num)
            if key is not None:
                return [index, key]
            dic[num] = index
        return


# @lc code=end
