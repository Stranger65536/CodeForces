_, arr = input(), sorted([int(i) for i in input().split()], reverse=True)
print([(sum(arr[:(idx + 1)]) > sum(arr[(idx + 1):])) for idx, i in enumerate(arr)].index(True) + 1)
