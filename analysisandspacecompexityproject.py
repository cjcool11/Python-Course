def myfunction1(n):
    if n > 0:
        print("Base case reached: n > 0")
        return
    for i in range(0, n+1):
        print("Codingal")
    myfunction1(n // 2)
    myfunction1(n // 3)

def analyze_myfunction1_complexity(n):
    print("Analyzing myfunction1 complexity for n =", n)
    print("Recurrence Relation: T(n) = O(n) + T(n/2) + T(n/3)")
    print("Time Complexity: O(n log n)")
    myfunction1(n)

analyze_myfunction1_complexity(10)


def myfunction2(n):
    if n <= 1:
        print("Base case reached: n <= 1")
        return
    print("Codingal")
    myfunction2(n + 1)

def analyze_myfunction2_complexity(n):
    print("Analyzing myfunction2 complexity for n =", n)
    print("Recurrence Relation: T(n) = O(1) + T(n+1)")
    print("Time Complexity: O(infinite)")

analyze_myfunction2_complexity(15)
