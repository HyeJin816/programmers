import heapq

def solution(operations):
    H = []
    for i in operations:
        ### 숫자 삽입
        if i[0]=='I':
            heapq.heappush(H, int(i[2:]))
        elif not H:
            continue
        ### 최솟값 삭제
        elif i == 'D -1':
            heapq.heappop(H)
        ### 최댓값 삭제
        else:
            R = []
            for h in H:
                heapq.heappush(R, -h)
            heapq.heappop(R)
            print("R", R)
            H = []
            for r in R:
                heapq.heappush(H, -r)
            print("Change", H)
    if not H:
        return [0, 0]
    else:
        return [max(H), min(H)]
