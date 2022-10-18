def solution(m, n, puddles):
    ### 전체 grid 생성
    grid = [ [0]*(m+1) for _ in range(n+1) ]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0 or [j, i] in puddles:
                grid[i][j] = 0
            elif i == 1 and j == 1:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
    return (grid[n][m]% 1000000007)
