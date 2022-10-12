def solution(arr1, arr2):
    l1, l2, m, n = len(arr1), len(arr2[0]), 0, 0
    #미리 배열 만들어주기
    answer = [[i for i in range(l2)] for j in range(l1)]
    print(answer)
    while m < l1:
        answer[m][n] = 0
        for i in range(len(arr2)):
            answer[m][n] += arr1[m][i] * arr2[i][n]
        m = m+1 if n==l2-1 else m
        n = n+1 if n<l2-1 else 0
    return answer
