n =int(input())
lst=[]

for i in range(n):
    temp = int(input())
    lst.append(temp)

print(int(sum(lst)/n))
