class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes_removed_set = set(nums)

        if len(dupes_removed_set) == len(nums):
            return False
        return True