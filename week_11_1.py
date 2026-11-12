#문자열 슬라이싱
#[start:end:step]
'''s = 'Monty Python'
print(s[::])#시작이 0이고 끝이 12stap 1'''


'''s='Monty 7724'
#어떠한 문자에서열도 뒤에서 4자리 출력 코드 
print(s[-4:])#s[-4::]'''

#이름이 2글자인 경우 노채ㅣ 기회를 ㅣ 룰 추가

'''student='26730029노채영소프트웨어학과'
s_id=student[:8]
name=student[8:11]
major=student[-7:]

print('학번:',s_id)
print('이름:',name)
print('학과:',major)'''


student='26730029노채영|소프트웨어학과'
student1='26730029노채|소프트웨어학과'
student2='26730029노|소프트웨어학과'

'''pos=student1.find('|')
print(pos)

s_id=student1[:8]
name=student1[8:pos]
major=student1[-7:]

print('학번:',s_id)
print('이름:',name)
print('학과:',major)'''


pos=student2.find('|')
print(pos)

#if len(student)==17:
    
s_id=student2[:8]
name=student2[8:pos]
major=student2[pos+1:]

print('학번:',s_id)
print('이름:',name)
print('학과:',major)
