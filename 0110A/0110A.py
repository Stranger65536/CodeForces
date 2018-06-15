print('YES' if all((i in ['4', '7'] for i in str(sum((1 for i in input() if i in ['4', '7']))))) else 'NO')
