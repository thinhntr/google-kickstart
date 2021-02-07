def print_result(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().split()))


def idx_of(key):
    return ord(key) - ord("A")


def key_of(idx):
    return chr(idx + ord("A"))


def insert_link(adj_mat, start, end):
    end_idx = idx_of(end)
    start_idx = idx_of(start)

    if start_idx == end_idx:
        return

    if adj_mat[start_idx][end_idx] == 0:
        adj_mat[start_idx][end_idx] = 1
        adj_mat[start_idx][-1] += 1
        adj_mat[-1][end_idx] += 1


def solve(order):
    R, C = read_ints()

    S = []
    for _ in range(R):
        S.append(readln())

    adj_mat = [[0 for _ in range(27)] for _ in range(27)]
    unvisited = set()
    is_valid = True

    for col in range(C):
        prev_node = S[-1][col]
        unvisited.add(idx_of(prev_node))
        added_node = set()
        for row in reversed(range(R)):
            node = S[row][col]
            if node == prev_node:
                continue
            added_node.add(prev_node)
            if node in added_node:
                is_valid = False
            if not is_valid:
                break
            unvisited.add(idx_of(node))
            insert_link(adj_mat, prev_node, node)
            prev_node = node
            
        if not is_valid:
            break

    if not is_valid:
        print_result(order, -1)
        return

    
    trace = []
    node = -1

    while len(unvisited) != 0:
        if node == -1:
            for i in unvisited:
                if adj_mat[-1][i] == 0:
                    node = i
                    break
        
        if node != -1:
            unvisited.remove(node)
            trace.append(key_of(node))
            
        min_in_link = 26
        min_node = -1
        for i in unvisited:
            if adj_mat[node][i] != 0:
                if adj_mat[-1][i] < min_in_link:
                    min_in_link = adj_mat[-1][i]
                    min_node = i
        node = min_node

    print_result(order, "".join(trace))


if __name__ == "__main__":
    T = read_int()
    for t in range(T):
        solve(t)
