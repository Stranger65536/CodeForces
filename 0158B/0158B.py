n, (a, b, c, d) = int(input()), map(input().split().count, ['1', '2', '3', '4'])
print((max(a - c, 0) + b * 2 + 3) // 4 + c + d)
