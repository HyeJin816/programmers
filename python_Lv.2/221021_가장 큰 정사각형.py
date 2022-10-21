import numpy as np

def solution(board):
    clear_x = change(board, MAXnum(board))
    
    if MAXnum(clear_x) == 1:
        return 1
    elif MAXnum(clear_x) == 0:
        return 0
    
    new = (np.array(clear_x)).transpose()
    new = new.tolist()
    clear_y = change(new, MAXnum(new))
    
    return MAXnum(clear_y)**2
    
### 최대 정사각형이 들어갈 수 없으면 전체 0으로 변환    
def change(board,answer):
    for line in range(len(board)):
        if sum(board[line]) < answer:
            board[line] = [0] * len(board[line])
    return board

### 전체 합으로 최대 정사각형 크기 반환
def MAXnum(board):
    num = 0
    for x in board:
        num += sum(x)
    return int(num**(1/2))
