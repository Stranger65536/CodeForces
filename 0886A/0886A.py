a = list(map(int, input().split()))


def calc(a):
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if i != j and j != k and i != k:
                    left = {i, j, k}
                    right = set(range(6)) - left
                    s_left = sum((a[i] for i in left))
                    s_right = sum((a[i] for i in right))
                    if s_left == s_right:
                        return 'YES'
        return 'NO'


print(calc(a))
