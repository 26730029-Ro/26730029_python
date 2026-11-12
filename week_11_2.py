#문자 자료형+ 문자 자료형 ->연결
'''print('k'+'l')

#in, not in
#A in B-> A라는게 B에 존재하는지
#A not in B ->A라는게 B에 존재하지 않는지 
print('H' in 'hello')
print('H' not in 'hello')



#회문 구하기 
a='python'
b=a[::-1]

if a==b:
    print('회문 입니다')
else:
    print('회문이 아닙니다')'''



#input 표준 입력함수 (키보드-> 변수 저장)


'''response = input('게임을 계속하시겠어요?')
if response.lower() == 'yes':
        print('게임을 계속합니다.')
else:
        print('다음에 또 뵈요.')


while True:
    password = input('새로운 패스워드를 선택하시오 (문자와 숫자만 가능): ')
    if password.isalnum():
        print("정상")
    else:
        print('문자와 숫자만을 이용하여 패스워드를 선택하시오.')'''

'''print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())'''

# startswith(s) s로 시작하는지 검사
# endswith(s) s로 끝나는지 검사 (확장명 검사)
#split() -> 리스트
'''string='welcome to python'
string=string.split()#()기본값 공백 split('')
print(string)'''

string2='welcome/to/python'
string2=string2.split('/')
print(string2)


#문자열을 하나의 문자 요소들로 변환 list()
string3='welcome to python'
string3= list(string3)
print(string3)


#문자열을 하나의 문자 요소들로 변환 list() 공백은 빼고
#replace(),join()

string='welcome to python'
string= list(string.replace("",""))
print(string)
        





