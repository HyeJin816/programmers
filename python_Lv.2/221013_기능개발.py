def solution(progresses, speeds):
    ### 남은작업
    rest = [100-x for x in progresses]
    
    ### 소요날짜
    days = [r//s for r,s in zip(rest,speeds)]       
    for i in range(len(speeds)):
        if rest[i] % speeds[i] > 0:
            days[i] += 1
            
    ### 배포차례
    stack = days[0]
    answer = [1]
    for j in range(1,len(days)):
        if days[j] > stack:
            answer.append(1)
            stack = days[j]
        else:
            answer[-1] += 1 
    return answer
