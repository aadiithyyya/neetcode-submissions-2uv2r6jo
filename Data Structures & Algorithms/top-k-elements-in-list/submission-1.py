from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = Counter(nums)
        sorted_arr = sorted(arr.items(), key=lambda x: x[1], reverse=True)
        res = []

        for i in range(k):
            res.append(sorted_arr[i][0])
            
        return res

            




        