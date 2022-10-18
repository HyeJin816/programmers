import heapq

def solution(n):
    answer = []
    heapq.heapify(answer)
    heapq.heappush(answer, 1)
    heapq.heappush(answer, 2)
    for i in range(2,n+1):
        a = heapq.heappop(answer) 
        b = heapq.heappop(answer) 
        heapq.heappush(answer, b)
        heapq.heappush(answer, a+b)
        
    return heapq.heappop(answer)%1000000007
