### 소수인지 확인
def check(number):
    if (number == '1') or (number == '') :
        return False
    number = int(number)
    for n in range(2,int(number**(1/2))+1):
        if number % n ==0:
            return False
    return True


### k진수로 변환
def change(number,k):
    answer = ''
    while number:
        answer = str(number%k) + answer
        number = number//k
    return answer


def solution(n, k):

    ### k진수로 변환
    new_n = change(n,k)

    ### 0을 제외한 숫자 추출
    nums = []
    num = ''
    for i in (new_n+'0'):
        if i == '0':
            nums.append(num)
            num = ''
        else:
            num = num + i

    ### 추출된 숫자 중 소수만 반환
    answer = []
    for j in nums:
        if check(j) == True:
            answer.append(j)

    return len(answer)
