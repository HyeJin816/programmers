import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        ### 불가능 예외 처리
        if len(scoville) < 2:
            return -1
        num = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, num)
        count += 1
    return count
