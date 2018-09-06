i = int(input())
for j in range(i + 1, 10000):
    if len({j // 1000, j % 1000 // 100, j % 100 // 10, j % 10}) == 4:
        print(j)
        break
