def fun1(N, M):
    return N * M

def fun2(N, M):
    result = 0
    for _ in range(M):
        result += N
    return result

N = 23
M = 59

print("Result using single iteration function:", fun1(N, M))
print("Result using N iterations function:", fun2(N, M))
