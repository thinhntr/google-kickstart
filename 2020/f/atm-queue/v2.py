from math import ceil
T = int(input().strip())
for t in range(1, T + 1):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    order = list(
        map(
            lambda it: (ceil(it[1] / X), it[0]), 
            enumerate(A, 1)
        )
    )
    
    order.sort()
    
    print(f"Case #{t}: {' '.join(map(lambda it: str(it[1]), order))}")
    