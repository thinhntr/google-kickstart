def printRes(order, result):
    print(f"Case #{order + 1}: {result}")

def readln():
    return input().strip()
    
def readInt():
    return int(input().strip())

def readInts():
    return list(map(int, input().split()))

def solve(order):
    N, K, S = readInts()
    option1 = K - 1 + (K - S) + (N - S + 1)
    option2 = K + N
    
    printRes(order, min(option1, option2))

if __name__ == "__main__":

    T = readInt()
    for t in range(T):
        solve(t)
