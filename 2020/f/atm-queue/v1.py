from collections import deque
T = int(input().strip())
for t in range(1, T + 1):
    N, X = map(int, input().split())
    A = deque(map(int, input().split()))
    ids = deque([_ for _ in range(1, N + 1)])
    leaved_ids = deque()
    while N > 0:
        if A[0] <= X:
            A.popleft()
            leaved_ids.append(ids.popleft())
            N -= 1
        else:
            A[0] -= X
            A.append(A.popleft())
            ids.append(ids.popleft())

    print(f"Case #{t}: {' '.join(map(str, leaved_ids))}")