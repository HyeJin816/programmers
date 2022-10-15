def solution(land):
    answer = []
    for a in range(1,len(land)):
        for b in range(4):
            point = land[a][b] + max(land[a-1][(b+1)%4],
                                     land[a-1][(b+2)%4],
                                     land[a-1][(b+3)%4])
            land[a][b] = point
    return max(land[-1])
