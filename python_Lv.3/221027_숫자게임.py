import heapq

def solution(A, B):

    ### B팀이 절대 이기지 못하는 경우
    if min(A) >= max(B):
        return 0

    ### 이긴 횟수 구하기
    answer = 0
    newA = [-a for a in A]
    newB = [-b for b in B]
    heapq.heapify(newA)
    heapq.heapify(newB)

    while newA:
        a = heapq.heappop(newA)
        b = heapq.heappop(newB)
        if -a < -b:
            answer += 1
        else:
            heapq.heappush(newB, b)

    return answer
