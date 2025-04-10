def find_paths(n, m, path=[], x=0, y=0):
    if x == n - 1 and y == m - 1:
        print(path)
        return
    if x < n - 1:
        find_paths(n, m, path + ["Down"], x + 1, y)
    if y < m - 1:
        find_paths(n, m, path + ["Right"], x, y + 1)

n = 3
m = 3
find_paths(n, m)