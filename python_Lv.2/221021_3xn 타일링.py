import heapq

def solution(n):
  
    if n%2:
        return 0
      
    answer = []
    heapq.heapify(answer)
    heapq.heappush(answer,1) ## n=0
    heapq.heappush(answer,3) ## n=2

    for i in range(1,n//2+1):
        f_4 = heapq.heappop(answer)
        f_2 = heapq.heappop(answer)
        heapq.heappush(answer, f_2)
        heapq.heappush(answer, f_2*4-f_4)

    return heapq.heappop(answer)%1000000007
