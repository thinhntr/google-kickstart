
def printRes(order, result):
    print(f"Case #{order + 1}: {result}")

def readln():
    return input().strip()
    
def readInt():
    return int(input().strip())

def readInts():
    return list(map(int, input().split()))

def solve(order):
    N = readInt()
    V = readInts()
    met_nums = set()
    current_max = V[0]
    count = 0
    for i in range(N):
        current_max = max(current_max, V[i])
        if V[i] != current_max or V[i] in met_nums:
            continue
        met_nums.add(V[i])
        if i == N - 1 or V[i] > V[i + 1]:
            count += 1

    printRes(order, count)

if __name__ == "__main__":

    T = readInt()
    for t in range(T):
        solve(t)
