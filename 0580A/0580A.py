n, a = int(input()), list(map(int, input().split()))
strike = 1
max_strike = 1
for i in range(n - 1):
    if a[i + 1] < a[i]:
        strike = 1
    else:
        strike += 1
        max_strike = strike if strike > max_strike else max_strike

print(max_strike)
