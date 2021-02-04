T = int(input().strip())

for t in range(1, T + 1):
    N = int(input().strip())
    V = list(map(int, input().split()))
    max_from_left = [V[0]] * N
    for i in range(1, N):
        max_from_left[i] = max(V[i], max_from_left[i-1])

