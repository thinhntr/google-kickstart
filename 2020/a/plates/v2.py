# dynamic programming version



def solve(n, k, p):
    dp = [[0] * (p + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, p + 1):
            for x in range(min(j, k) + 1):
                dp[i][j] = max(dp[i][j], prefix_arr[i-1][x] + dp[i-1][j-x])
    return dp[n][p]



if __name__ == "__main__":
    T = int(input().strip())
    for t in range(1, T + 1):
        N, K, P = map(int, input().split())

        prefix_arr = []
        for _ in range(N):
            row = list(map(int, input().split()))
            for k in range(1, K):
                row[k] += row[k - 1]
            row.insert(0, 0)
            prefix_arr.append(row)
        
        print(f"Case #{t}: {solve(N, K, P)}")