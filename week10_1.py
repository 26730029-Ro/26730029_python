#set 고유한 값을 가진다,순서가 없다 
'''b=[1,2,3,1,2,3,1,2,3]
a=set(b)
print(*a)'''

#len()의 개수반환 
'''fruits={'apple','banana','grape'}
size=len(fruits)
print(size)'''


#포함되는지
'''string=input()
fruits={'apple','banana','grape'}
if string in fruits:
    print(string,'있습니다')

else:
    (string,'없습니다')'''

#출력 (무작위로 출력 ) 
'''fruits={'apple','banana','grape'}
print(fruits)'''


#출력( 출력시 정렬해서 출력할수는 있음)
'''fruits={'apple','banana','grape'}
for x in sorted(fruits):
    print(x,end='')


#add() 요소추가,삭제 
fruits={'apple','banana','grape'}
fruits.add('kiwi')
print(fruits)
fruits.remove('kiwi') #discard()
print(fruits)'''

