def printresult(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def readint():
    return int(input().strip())


def readints():
    return list(map(int, input().split()))


def solve(order):
    N = readint()
    A = readints()

    if N < 4:
        printresult(order, N)
        return

    D = [0 for _ in range(N)]
    count = [0 for _ in range(N)]

    D[0] = A[1] - A[0]
    count[0] = 1
    maxl = 0

    for i in range(1, N):
        D[i] = A[i] - A[i - 1]
        count[i] = 1 if D[i] != D[i - 1] else count[i - 1] + 1
        maxl = max(maxl, count[i])

    for i in reversed(range(N)):
        if count[i] == i + 1:
            break
        currentLength = count[i]
        type1 = currentLength + 2
        while count[i] > 1:
            i -= 1
        type2 = 0
        type3 = 0
        type4 = 0
        if i - 3 >= 0 and D[i - 3] == D[i] and A[i - 3] + D[i - 3] * 2 == A[i - 1]:
            type2 = currentLength + count[i - 3] + 2
            if count[i - 3] < i - 2:
                type2 += 1
        if i == N - 1 or i < N - 1 and count[i + 1] == 1 and D[i - 1] == D[i - 2]:
            type3 = count[i - 1] + 1
        if i - 2 >= 0 and A[i - 2] + D[i - 2] * 2 == A[i]:
            type4 = count[i - 2] + 2
        maxl = max(maxl, type1, type2, type3, type4)
    printresult(order, maxl)


if __name__ == "__main__":
    T = readint()
    for t in range(T):
        solve(t)
