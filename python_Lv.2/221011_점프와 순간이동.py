### 221011_점프와 순간이동

def solution(n):
    ans = 0
    while n:
        if n%2==0:
            n=n/2
        else:
            ans+=1
            n=(n-1)/2
    return ans
