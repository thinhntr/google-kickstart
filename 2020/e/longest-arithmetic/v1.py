T = int(input().strip())
for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    count_sub = 1
    max_sub = 0
    next_val = A[0] - A[1]
    for i in range(N - 1):
        current_val = A[i] - A[i + 1]
        
        if current_val == next_val:
            count_sub += 1
        else:
            count_sub = 2

        max_sub = max(max_sub, count_sub)
        next_val = current_val
    
    print(f"Case #{t}: {max_sub}")