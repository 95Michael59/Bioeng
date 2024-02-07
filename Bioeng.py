#Fibonacci algorithms

#Slow algorithm. O(2^n)
def fibonacci1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci1(n-1)+fibonacci1(n-2)
x = int(input())
print(fibonacci1(x))

#Faster algorithm. O(n^2)
def fibonacci2(n):
    if n == 0:
        return 0
    f = []
    for j in range(n + 1):
        f.append(0)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
x = int(input())
print(fibonacci2(x))

