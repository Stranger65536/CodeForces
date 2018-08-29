n, a = int(input()), sorted(map(int, input().split()))
print(sum((abs(n + 1 - ai) for n, ai in enumerate(a))))
