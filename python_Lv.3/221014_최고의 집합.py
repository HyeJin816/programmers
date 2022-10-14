def solution(n, s):
    if n > s:
        return [-1]
    num = s//n
    answer = [num]*n
    for i in range(s%n):
        answer[i] += 1
    ### 오름차순 정렬
    answer.sort()
    return answer
