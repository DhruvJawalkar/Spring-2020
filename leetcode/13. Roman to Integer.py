class Solution:
def romanToInt(self, s: str) -> int:
    numeral_to_val = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    base_val = 10000
    num = 0
    
    for d in s:
        if(numeral_to_val[d]<=base_val):
            num += numeral_to_val[d]
            base_val = numeral_to_val[d]
        else:
            num -= base_val
            num += (numeral_to_val[d] - base_val)
            base_val = numeral_to_val[d]
            
    return num        
