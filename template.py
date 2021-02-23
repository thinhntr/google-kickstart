def printresult(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def readint():
    return int(input().strip())


def readints():
    return list(map(int, input().split()))


def solve(order):
    print_result(order, "#TODO")


if __name__ == "__main__":
    T = readint()
    for t in range(T):
        solve(t)
