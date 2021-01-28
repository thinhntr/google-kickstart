def takesum(prefix_arr, counters):
    total = 0
    for i, count in enumerate(counters):
        if count <= 0:
            continue
        total += prefix_arr[i][count - 1]
    return total

