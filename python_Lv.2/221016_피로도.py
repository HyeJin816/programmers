from collections import deque

def solution(k, dungeons):
    L = len(dungeons)
    count = 0
    dp = deque()
    dp.append([k,[]])

    while dp:
        k,visit = dp.popleft()
        for i in range(L):
            [a,b]=dungeons[i]
            if (i not in visit) and (k >= a) and (k-b > 0): 
                dp.append([k-b, visit+[i]])
            else : 
                count = max(count, len(visit))
    return count
