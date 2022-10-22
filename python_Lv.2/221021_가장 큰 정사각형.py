def solution(board):
    count = 0
    lb = len(board)
    lr = len(board[0])

    if (lb<2) or (lr<2):
        return 1

    for r in range(1,lb):
        for c in range(1,lr):
            if board[r][c] != 0:
                board[r][c] = min(board[r][c-1], board[r-1][c], board[r-1][c-1])+1
                count = max(count, board[r][c])
                
    return count**2
