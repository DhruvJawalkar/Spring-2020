class Solution:
def findJudge(self, N: int, trust: List[List[int]]) -> int:
    #in-degree - out-degree == N-1
    
    in_out = [0]*(N+1)
    
    for trust_pair in trust:
        in_out[trust_pair[1]] +=1
        in_out[trust_pair[0]] -=1
    
    for p in range(1, N+1):
        if(in_out[p]==N-1):
            return p
    
    return -1
    

