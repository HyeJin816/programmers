### 정확성 모두 통과 / 효율성 실패 ###
def solution(prices):
    answer = []
    while prices:
        if prices[0] <= min(prices):
            answer.append(len(prices)-1)
        else:
            check = [x - prices[0] for x in prices]
            num = [n for n in check if n<0]
            idx = check.index(num[0])
            answer.append(idx)
        prices = prices[1:]
    return answer
###################################
    
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        # 끝까지 안떨어지는 경우
        time = len(prices) - i -1
        # 중간에 떨어지는 경우
        for i_p in range(i+1,len(prices)):
            if prices[i_p] < prices[i]:
                time = i_p - i
                break
        answer.append(time)
    answer.append(0)
    return answer
