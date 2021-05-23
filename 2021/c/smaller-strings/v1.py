def printresult(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def readint():
    return int(input().strip())


def readints():
    return list(map(int, input().split()))


def hashc(c):
    return ord(c) - 96


MOD = int(10e9 + 7)


def power(base, exp):
    """Fast power calculation using repeated squaring"""
    ans = 1
    while exp:
        if exp & 1:
            ans = (ans * base) % MOD
        exp >>= 1
        base *= base
    return ans % MOD


def solve(order):
    N, K = readints()
    S = readln()
    if N == 1:
        printresult(order, hashc(S) - 1)
        return
    if N == 2:
        f, s = hashc(S[0]), hashc(S[1])
        printresult(order, min(f, s))
        return

    total = 0
    mid = N // 2
    if N % 2 == 0:
        mid -= 1
    all_good = True
    for i in reversed(range(mid)):
        if S[i] < S[N - i - 1]:
            all_good = False
            break
    if N % 2 == 0:
        total = hashc(S[mid]) if S[mid] < S[N - mid - 1] else hashc(S[N - mid - 1])
        print(S[mid], hashc(S[mid]))
        if not all_good:
            total -= 1
        print(total)
        for i in reversed(range(mid)):
            total = ((hashc(S[i]) - 1) * power(K, mid - i) + total) % MOD
    else:
        pass

    printresult(order, total)


if __name__ == "__main__":
    T = readint()
    for t in range(T):
        solve(t)
