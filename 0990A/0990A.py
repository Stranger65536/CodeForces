n, m, a, b = [int(i) for i in input().split(' ')]
add = (n // m * m + m - n) * a
rem = (n - n // m * m) * b
print(min(add, rem) if n % m != 0 else 0)
