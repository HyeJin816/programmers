### 정확성 모두 통과 / 효율성 실패 ###

def solution(n, works):
    ### 남은 작업량이 없는 경우
    if sum(works) < n:
        return 0
    
    ### 작업량 계산
    for _ in range(n):
        works.sort(reverse=False)
        works[-1] -= 1
    
    ### 피로도 계산
    answer = 0
    for j in works:
        answer += j*j
    
    return answer
###################################


##### 정확성 & 효율성 모두 통과 #####
  
import heapq

def solution(n, works):
    ### 남은 작업량이 없는 경우
    if sum(works) < n:
        return 0

    ### 작업량 계산
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        num = heapq.heappop(works)
        num += 1
        heapq.heappush(works, num)

    ### 피로도 계산
    answer = []
    for j in works:
        heapq.heappush(answer, j*j)

    return sum(answer)
  
