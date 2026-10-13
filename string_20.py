password = input()
pattern = input()

r_pattern = pattern * 5


if password in r_pattern:
    print('YES')
else:
    print('NO')
