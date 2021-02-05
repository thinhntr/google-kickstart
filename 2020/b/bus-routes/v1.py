def print_result(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().split()))


def solve(order):
    _, D = read_ints()
    X = read_ints()
    L = D
    for x in reversed(X):
        L -= L % x

    print_result(order, L)


if __name__ == "__main__":
    T = read_int()
    for t in range(T):
        solve(t)
