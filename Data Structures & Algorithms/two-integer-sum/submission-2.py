class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h={}
        for i, val in enumerate(nums):
            val_in_h = target - val

            if val_in_h in h:
                return [h[val_in_h],i]
            
            h[val]=i
        
            

            