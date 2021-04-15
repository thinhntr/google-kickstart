def printresult(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def readint():
    return int(input().strip())


def readints():
    return list(map(int, input().split()))


def solve(order):
    N, K = readints()
    S = readln()
    gn = 0
    for i in range(0, N // 2):
        if S[i] != S[N-i-1]:
            gn += 1
    printresult(order, abs(K - gn))


if __name__ == "__main__":
    T = readint()
    for t in range(T):
        solve(t)
