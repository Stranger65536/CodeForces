n = 5
pos = [input().find('1') // 2 + 1 for i in range(n)]
print([abs(n // 2 + 1 - i) + abs(n // 2 - idx) for idx, i in enumerate(pos) if i][0])
