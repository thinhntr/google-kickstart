# brute force version

def takesum(counters):
    total = 0
    for i, count in enumerate(counters):
        if count <= 0:
            continue
        total += prefix_arr[i][count - 1]
    return total


def solve(n, k, p):
    n_plates = [0] * n
    total_plates = 0
    i = n - 1
    while i >= 0:
        if i == n - 1:
            if total_plates == p:
                max_beauty[0] = max(max_beauty[0], takesum(n_plates))
        if n_plates[i] == k:
            total_plates -= n_plates[i]
            n_plates[i] = 0
            i -= 1
        else:
            total_plates += 1
            n_plates[i] += 1
            i = n - 1


if __name__ == "__main__":
    T = int(input().strip())
    for t in range(1, T + 1):
        N, K, P = map(int, input().split())

        prefix_arr = []
        for _ in range(N):
            row = list(map(int, input().split()))
            for k in range(1, K):
                row[k] += row[k - 1]
            prefix_arr.append(row)
        
        max_beauty = [0]
        solve(N, K, P)

        print(f"Case #{t}: {max_beauty[0]}")