#1
print('신씨가 소리질렀다. "도둑이야".')

#2
print("Mary's cosmetics")


#3 print(sep='')
print(1,2,3,4,5,6, sep='/')


#7
print('naver','kakao','sk','samsung', sep=';')

#9
print("first", end='');print("second")


#type값의 타입을 알려주는 함수

'''a=123#int정수 
print(type(a))

a='123'#str문자열 
print(type(a))

a=12.4 
print(type(a))#float실수 '''


#문자를 정수로 바꾸는 방법
a='123'
#대입해서 변수를 int변경 
a=int(a)
#변수에 데이터타입을 변경하지 않고 변경
print(type(int(a)))#순간적 변경!

#정수->실수
b=123
b=float(b)

#정수->문자
c=124
c=str(c)
#문자열 인덱싱->pt
x='python'
print(x[0],x[2])
#문자열 슬라이싱 ->뒤에 4자리
z='안녕하세요 1234'
print(z[-4::])

#문자열 슬라이싱 step
string = "홀짝홀짝홀짝"
print(string[::2])

#문자열 슬라이싱 거꾸로 출력
string = "PYTHON"
print(string[::-1])

#replace 치환된 새로운 문자열이 리턴
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")# 첫번째'-'은 교체할 값
print(phone_number1)


#python300제 27  split함수 사용 
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])


#문자+문자(더하기 연산 -> 연산 )
a='3'
b='2'
print(a+b)

#문자 * 숫자 (곱하기-> 문자를 숫자만큼 반복해서 출력)
a='hi'
print(a*10)

#문자열 곱하기 34번 문제 
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
#print((t1+' '+t2+' ')*4))


#38번 (콤마 제거 후 정수 형변환)
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))

#40번 strip()은 좌우 공백을 제거
data = "   삼성전자    "
print(data.strip())

# "2020-05-01"연도, 월, 일로 나눠보세요
date = "2020-05-01"
temp = data.split('-')
year=temp[0]
month=temp[1]
day=temp[2]
print(yeal)
print(month)
print(day)

#051 리스트 생성
movieas = ["닥터 스트레인지", "스플릿", "럭키"]

#리스트의 원소 추가 ->append('값')-맨 뒤에 값을 추가
movies = ["닥터 스트레인지", "스플릿", "럭키"]
movies.append("배트맨")
print(movies)

#53 리스트에 원소를 추가하는데 특정위치에 추가 insert()(인덱스,값)
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")

#54리스트 원소 삭제 (remove('값'),del리스트이름[인덱스],pop(인덱스)
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

movie_rank.remove('럭키')
del movie_rank[3]

#56리스ㅌ의 합(더하기 연산)*중복허용 
a=['a','b','c']
b=['a','b','c']
c=a+b

#57 리스트값중에 최대값(max()),최소값(min())
a_list=[1,2,3,4,5,6,7,8]
print(max(a_list))
print(min(a_list))

#58 리스트 요소값에 합 (sum())
print(sum(a_list))

#59 리스트 요소에 개수 (len())
print(len(a_list))

#60 리스트 요소값 평균 (sum()/len())
print(sum(a_list)/len(a_list))

