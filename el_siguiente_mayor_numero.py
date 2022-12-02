def next_bigger(n):
    n = str(n)
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            n = n[:i-1] + n[i] + n[i-1] + n[i+1:]
            return int(n)
    return -1