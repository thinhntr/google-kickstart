def solve():
    T = int(input())
    for t in range(1, T + 1):
        N, B = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        count = 0
        for price in A:
            B -= price
            if B >= 0:
                count += 1
            else:
                break
        print(f"Case #{t}: {count}")

solve()