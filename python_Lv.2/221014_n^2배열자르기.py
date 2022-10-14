def solution(n, left, right):
    l1, l2 = left//n, left%n
    r1, r2 = right//n, right%n
    answer = []
    for i in range(l1,r1+1):
        line = [i+1]*(i)
        for j in range(n-i):
            line.append(i+j+1)
        answer += line
    ### 결과 출력
    if r2==n-1:
        return answer[l2:]
    else:
        return answer[l2:-(n-1-r2)]
