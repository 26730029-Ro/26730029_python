count = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num % 2 == 0:
        count += 1

print(count)
