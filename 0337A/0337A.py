m, n = map(int, input().split())
a = sorted(map(int, input().split()))
print(min((a[i + m - 1] - a[i] for i in range(n - m + 1))))
