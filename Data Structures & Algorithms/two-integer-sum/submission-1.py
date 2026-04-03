class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_sol = {}
        for i, val in enumerate(nums):
            needed = target - val
           
            if needed in hashmap_sol:
                return [hashmap_sol[needed],i]    
                
            hashmap_sol[val]=i

        
            

            