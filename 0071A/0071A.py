n = int(input())
for i in range(n):
    s = input()
    print(s[0] + str(len(s) - 2) + s[-1] if len(s) > 10 else s)
