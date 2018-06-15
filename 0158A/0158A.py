n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
print(sum(1 for x in a if x >= a[k - 1] and x))
