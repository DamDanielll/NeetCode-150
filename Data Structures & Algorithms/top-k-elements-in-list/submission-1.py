class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = []
        counts = []        
        for i, num in enumerate(nums):
            if num not in vals:
                vals.append(num)
                counts.append(1)
            else:
                counts[vals.index(num)]+=1
        res = []
        while k > 0:
            high_idx = counts.index(max(counts))
            res.append(vals[high_idx])
            del counts[high_idx]
            del vals[high_idx]
            k-=1
        return res
            

        
