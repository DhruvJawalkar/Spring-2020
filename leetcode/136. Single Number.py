from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = defaultdict(lambda:False)
        
        for item in nums:
            if(not seen[item]):
                seen[item] = True
            elif(seen[item]):
                del seen[item]
                
        res = list(seen.keys())
        return res[0]
