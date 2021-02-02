T = int(input().strip())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(None)
    j = K
    count = 0
    for num in A:
        if j == 0:
            count += 1
            j = K
        if num == j:
            j -= 1
        else:
            j = K
    print(f"Case #{t}: {count}")
