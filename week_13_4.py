#함수정의 def
def print_coin():
    print("비트코인")

#print_coin 함수를 100번호출하라
'''for _ in range(100):
    print_coin()'''

#함수 안에 문자열 100번 출력
'''def print_coins():
        print("비트"*100)
print_coins()'''


#함수에 인수를 전달 -> 함수이름('인수')
def fun(a) :
    print(a)
fun('hello') 
fun('world')

#하나의 문자 입력박아 뒤에 :D를 붙이시오
def print_smile(string):
    print(string+':D')
print_smile('안녕하세요')

#세개의 수를 입력받아 가장 큰 값 출력 함수
#삼항연산다를 사용 
def max_val(a,b,c):
    max_val= a
    max_val= b if b > max_val else max_val
    max_val= c if c > max_val else max_val
    return max_val

#하나의 딕셔너리를 입력받아 딕셔너리의 키값을 화면에 출력하는 print_keys함수를 정의하라
def print_keys(dic):
    for i in dic.keys():
        print(i)

print_keys({'이름':'홍길동','나이':30,'성별':0})

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)


#함수 -> 지역변수(그 안에서만 산다)

def n_plus_1 (n) :
    result = n + 1

print(n_plus_1(3))

# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는
# make_list 함수를 정의하라.

def make_list(string):
    return list(string)

print(make_list("abcd"))






