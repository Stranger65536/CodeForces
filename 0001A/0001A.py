import math

s = input()
n, m, a = [int(i) for i in s.split()]
print(int(math.ceil(n / a) * math.ceil(m / a)))
