print(sum(((lambda x, y: y - x >= 2)(*[int(i) for i in input().split()]) for i in range(int(input())))))
