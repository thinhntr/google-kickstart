def printRes(order, result):
    print(f"Case #{order + 1}: {result}")

def readln():
    return input().strip()
def readInt():
    return int(input().strip())

def readInts():
    return list(map(int, input().split()))

def solve(order):
    printRes(order)

if __name__ == "__main__":

    T = readInt()
    for t in range(T):
        solve(t)
