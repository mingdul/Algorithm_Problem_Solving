import sys
input = sys.stdin.readline

def n_queens(k):
    global count
    if k == n:
        count += 1
        return

    for col in range(n):
        if not (cols[col] or diag1[k + col] or diag2[k - col + n - 1]):
            cols[col] = diag1[k + col] = diag2[k - col + n - 1] = True
            n_queens(k + 1)
            cols[col] = diag1[k + col] = diag2[k - col + n - 1] = False

n = int(input().strip())
cols = [False] * n
diag1 = [False] * (2 * n - 1)  # k + col
diag2 = [False] * (2 * n - 1)  # k - col + n - 1
count = 0
n_queens(0)
print(count)
