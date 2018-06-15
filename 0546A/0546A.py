k, n, w = [int(i) for i in input().split()]
cost = k * (w + 1) * w // 2
print(cost - n if cost > n else 0)
