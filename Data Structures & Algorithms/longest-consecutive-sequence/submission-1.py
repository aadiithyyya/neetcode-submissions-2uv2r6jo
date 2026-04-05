class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new_nums = sorted(set(nums))
        count = 1
        default_longest = 1

        if not nums:
            return 0

        for i in range(1, len(new_nums)):

            if new_nums[i] == new_nums[i-1] + 1:
                count += 1

            else:
                default_longest = max(default_longest, count)
                count = 1

        return max(default_longest, count)