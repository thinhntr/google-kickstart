def printresult(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def readint():
    return int(input().strip())


def readints():
    return list(map(int, input().split()))


def get_range(f, s, ranges):
    for mrange in ranges[f]:
        minr, maxr = mrange
        if minr <= s and s <= maxr:
            return mrange
    return None


def get_rrange(r, c, rranges):
    return get_range(r, c, rranges)


def get_crange(r, c, cranges):
    return get_range(c, r, cranges)


def get_ranges(r, c, rranges, cranges):
    rrange = get_rrange(r, c, rranges)
    crange = get_crange(r, c, cranges)
    return rrange, crange


def count_l(r, c, rrange, crange):
    ll = c - rrange[0] + 1
    rr = rrange[1] - c + 1
    tt = r - crange[0] + 1
    bb = crange[1] - r + 1
    total = 0
    if ll > 1:
        maxlltt = max(ll, tt)
        minlltt = min(ll, tt)
        total += max(0, min(minlltt, maxlltt // 2) - 1)

        maxllbb = max(ll, bb)
        minllbb = min(ll, bb)
        total += max(0, min(minllbb, maxllbb // 2) - 1)
    if rr > 1:
        maxrrtt = max(rr, tt)
        minrrtt = min(rr, tt)
        total += max(0, min(minrrtt, maxrrtt // 2) - 1)

        maxrrbb = max(rr, bb)
        minrrbb = min(rr, bb)
        total += max(0, min(minrrbb, maxrrbb // 2) - 1)
    return total

def solve(order):
    R, C = readints()
    table = []
    
    for _ in range(R):
        table.append(readints())
    
    joints = set()

    rranges = [[] for _ in range(R)]
    cranges = [[] for _ in range(C)]

    for r in range(R):
        is_new_rrange = True
        for c in range(C):
            if table[r][c] == 1:
                if is_new_rrange:
                    rranges[r].append([c, c])
                    is_new_rrange = False
                else:
                    rranges[r][-1][1] = c

                if r > 0 and table[r-1][c] == 1:
                    rrange, crange = get_ranges(r - 1, c, rranges, cranges)
                    if crange is not None: 
                        crange[1] = r
                    
                    nc = c + 1
                    pc = c - 1
                    if rrange[1] > rrange[0]:
                        joints.add((r - 1, c))
                    elif pc > 0 and table[r][pc] == 1 or nc < C and table[r][nc] == 1:
                        joints.add((r, c))
                else:
                    cranges[c].append([r, r])
            else:
                is_new_rrange = True

    count_l_shape = 0
    for r, c in joints:
        rrange, crange = get_ranges(r, c, rranges, cranges)
        count_l_shape += count_l(r, c, rrange, crange)    
    printresult(order, count_l_shape)


if __name__ == "__main__":
    T = readint()
    for t in range(T):
        solve(t)
