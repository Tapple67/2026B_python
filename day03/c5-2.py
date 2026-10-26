# p.293 재귀함수, 재귀란 자기자신을 호출하는것
# 1] 팩토리얼 반복문
def factorial1(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return print(output)

factorial1(2) # 2! -> 1~ 2 -> 1*2
factorial1(3) # 3! -> 1~3 -> 1*2*3

# 2] 팩토리얼 재귀
def factorial2(n):
    if n == 0:
        return 1
    else:
        return n * factorial2(n-1)

print(factorial2(2))
print(factorial2(3))

# 만약에 n 이 3이면 n == = false
#  3* factorial2(2)
    # n 이 2이면 n==0 false
        # 2 * factorial2(1)
            # n이 1이면 n == 0 false
                # 1 * factorial2(0)
                    # n이 0이면 n==0 true
                        # 1

def 구구단(단=2,곱=1):
    if 단 > 9: 
        return
    if 곱 > 9 : # 곱하기 9까지 했으면 단 올리기
        구구단(단+1,1)
        return
    print( 단*곱)
    구구단(단,곱+1) # 곱 올리기

구구단()
                    

dictionary = {
    1:1,
    2:1
}

def finbonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = finbonacci(n-1) + finbonacci(n-2)
        dictionary[n] = output
        return output

print("finbonacci(10):", finbonacci(10))