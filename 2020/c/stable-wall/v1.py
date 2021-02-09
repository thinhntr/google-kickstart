def print_result(order, result):
    print(f"Case #{order + 1}: {result}")


def readln():
    return input().strip()


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().split()))


from collections import deque


def idx_of(key):
    return ord(key) - ord("A")


def key_of(idx):
    return chr(idx + ord("A"))


def insert_link(adj_mat, start, end):
    if start == end:
        return 

    end_idx = idx_of(end)
    start_idx = idx_of(start)

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
    nodes = set()

    for col in range(C):
        prev_key = S[-1][col]
        for row in reversed(range(R)):
            curr_key = S[row][col]
            insert_link(adj_mat, prev_key, curr_key)
            prev_key = curr_key

            curr_node = idx_of(curr_key)            
            nodes.add(curr_node)
            

    trace = []
    in_degrees = dict()
    queue = deque()
    visited = set()

    for node in nodes:
        in_degrees[node] = adj_mat[-1][node]  # store the in-degree of current node
        if in_degrees[node] == 0:
            queue.append(node)
            visited.add(node)

    while len(queue) != 0:
        curr_node = queue.popleft()

        curr_key = key_of(curr_node)
        trace.append(curr_key)

        for adj_node in range(26):
            if adj_mat[curr_node][adj_node] == 0:
                continue

            in_degrees[adj_node] -= 1
            
            if in_degrees[adj_node] == 0:
                queue.append(adj_node)
            
            visited.add(adj_node)

    if len(trace) != len(nodes):
        print_result(order, -1)
    else:
        print_result(order, "".join(trace))


if __name__ == "__main__":
    T = read_int()
    for t in range(T):
        solve(t)
