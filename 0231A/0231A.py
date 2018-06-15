n = int(input())
print(sum(input().count('1') >= 2 for i in range(n)))
