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
