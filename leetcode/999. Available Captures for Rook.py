class Solution:
def find_rook_position(self, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]=='R'):
                return (i,j)
    return (-1, -1)
    

def numRookCaptures(self, board: List[List[str]]) -> int:
    r_i, r_j = self.find_rook_position(board)
    can_capture = 0
    
    #up
    i, j = r_i, r_j
    j-=1
    while(j>=0):
        if(board[i][j]=='.'):
            j-=1
        elif(board[i][j]=='B'):
            break
        else:
            can_capture+=1
            break
    
    #down
    i, j = r_i, r_j
    j+=1
    while(j<=len(board)-1):
        if(board[i][j]=='.'):
            j+=1
        elif(board[i][j]=='B'):
            break
        else:
            can_capture+=1
            break
    
    #left
    i, j = r_i, r_j
    i-=1
    while(i>=0):
        if(board[i][j]=='.'):
            i-=1
        elif(board[i][j]=='B'):
            break
        else:
            can_capture+=1
            break
   
    #right
    i, j = r_i, r_j
    i+=1
    while(i<=len(board)-1):
        if(board[i][j]=='.'):
            i+=1
        elif(board[i][j]=='B'):
            break
        else:
            can_capture+=1
            break
            
    return can_capture
