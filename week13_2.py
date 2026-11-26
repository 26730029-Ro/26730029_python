#61번 날짜 정보를 빼고 출력 
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#리스트 요소 중에 홀수만 출력하기
nums = [1, 2, 3,4, 5, 6, 7, 8, 9, 10]
'''for i in nums:
    if i%2==1:
        print(i,end='')'''
   
#리스트 컴프리헨션
result=[n for n in nums if n%2==1]
'''for i in nums:
    if n%2==1'''#위에 한줄을 풀면 이럼

print(result)


#join메서드
#ex.단어 사이에 /를 추가하시
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest))

#('/')로 구분되어 하나의 문자열로 저장되어 있다 이를 리스트로 분리 저장하는법
#split메서드 문자열->리스트

string = "삼성전자/LG전자/Naver/sk하이닉스/미래에셋대우"
interest = string.split("/")
print(interest)

#리스트 정렬 (오름차순, 내림차순)
#sorted(리스트 이름)->sorted(리스트 이름,reverse=True)<-내림

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()#data.sort(revers=True)->내림차순
           #data.sort(revers=False)->오름차순 
print(data)


