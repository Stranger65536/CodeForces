n = int(input())
print('YES' if [i for i in [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777] if n % i == 0] else 'NO')
