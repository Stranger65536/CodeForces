m = k = 0
for i in range(int(input())):
    k -= eval(input().replace(' ', '-'))
    m = max(m, k)
print(m)
