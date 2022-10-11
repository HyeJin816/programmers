def solution(triangle):
    for i in range(1,len(triangle)):
        triangle[i-1].append(0)
        triangle[i][0] += triangle[i-1][0]
        for j in range(1,len(triangle[i])):
            a = triangle[i][j] + triangle[i-1][j]
            b = triangle[i][j] + triangle[i-1][j-1]
            triangle[i][j] = max(a,b)
        triangle[i-1].pop()
    return max(triangle[-1])
