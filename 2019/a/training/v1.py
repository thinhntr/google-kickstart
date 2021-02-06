def print_result(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().split()))


def get_sum(prefix_sum, start, end):
    if start == 0:
        return prefix_sum[end]
    return prefix_sum[end] - prefix_sum[start - 1]


def solve(order):
    N, P = read_ints()
    S = read_ints()

    S.sort()

    # Calculate prefix sum array
    prefix_sum = [S[0]] * N
    for i in range(1, N):
        prefix_sum[i] = S[i] + prefix_sum[i - 1]

    min_coaching_hours = S[N - 1] - S[0]    
    
    for i in range(N - P + 1):
        current_hours = S[i + P - 1] * (P - 1) - get_sum(prefix_sum, i, i + P - 2)
        min_coaching_hours = min(min_coaching_hours, current_hours)

    print_result(order, min_coaching_hours)


if __name__ == "__main__":
    T = read_int()
    for t in range(T):
        solve(t)
