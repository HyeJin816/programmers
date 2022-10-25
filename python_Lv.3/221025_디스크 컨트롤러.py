def solution(jobs):
    
    ### 작업요청시간&작업소요시간 범위
    sort_j = sorted(jobs, key=lambda x : x[1])
    for works in sort_j:
        if works[0] < 0 or works[0] > 1000:
            sort_j.remove(works)
        if works[1] < 1 or works[1] > 1000:
            sort_j.remove(works)
    
    ### 순서대로 처리
    start = 0
    answer = 0
    
    while sort_j:
        for j in range(len(sort_j)):
            if sort_j[j][0] <= start: 
                start += sort_j[j][1] 
                answer += start - sort_j[j][0] 
                sort_j.pop(j)
                break
            if j==len(sort_j)-1:
                start += 1

    return answer//len(jobs)
