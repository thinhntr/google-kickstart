T = int(input().strip())
for t in range(1, T + 1):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ids = [_ for _ in range(1, N + 1)]
    leaved_ids = []
    while len(A) > 0:
        if A[0] <= X:
            A.pop(0)
            leaved_ids.append(ids.pop(0))
        else:
            A[0] -= X
            A.append(A.pop(0))
            ids.append(ids.pop(0))

    print(f"Case #{t}: {' '.join(map(str, leaved_ids))}")