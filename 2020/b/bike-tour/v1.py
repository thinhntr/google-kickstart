if __name__ == "__main__":
    T = int(input().strip())
    for t in range(1, T + 1):
        N = int(input().strip())
        nums = list(map(int, input().split()))
        count = 0
        for i in range(1, N - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                count += 1
        print(f"Case #{t}: {count}")