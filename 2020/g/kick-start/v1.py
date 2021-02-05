def printRes(order, result):
    print(f"Case #{order + 1}: {result}")

def readln():
    return input().strip()

def readInt():
    return int(input().strip())

def readInts():
    return list(map(int, input().split()))

def solve(order):
    S = readln()
    kick = "KICK"
    start = "START"
    kick_len = len(kick)
    start_len = len(start)
    kick_count = 0
    count = 0
    for i in range(len(S) + 1):
        if i >= kick_len and S[i - kick_len:i] == kick:
            kick_count += 1
        if i >= start_len and S[i - start_len:i] == start:
            count += kick_count

    printRes(order, count)

if __name__ == "__main__":

    T = readInt()
    for t in range(T):
        solve(t)
