x,y= input().split()

start = ord(x)
end = ord(y)


for i in range(min(start, end), max(start, end) + 1):
    print(chr(i), end=' ')
