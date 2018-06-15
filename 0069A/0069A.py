print('YES' if not [i for i in [sum(i) for i in
                                list(map(list, zip(*[[int(i) for i in input().split()] for i in range(int(input()))])))]
                    if i] else 'NO')
