class Solution:
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    cur_greatest = max(candies)
    can_have_greatest = [False]*len(candies)
    
    for i, c in enumerate(candies):
        if(c+extraCandies>=cur_greatest):
            can_have_greatest[i] = True
    
    return can_have_greatest
    
