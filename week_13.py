#리스트 + 연산,(중복허용)
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs=lang1+lang2

print(langs)

#최값 max(),최소값 min() ,개수 len()

nums = [1, 2, 3, 4, 5,6,7]
print('최대값',max(nums),'최소값',min(nums),'개수',len(nums))
#리스트nums = [1, 2, 3, 4, 5]

print('리스트 요소의 합:',sum(nums))

#리스트는 중복을 허용 <-> set()
#중복된 데이터는 한번만 표시하세요
#예를 들어 다음 두 리스트를 하나로 합친 후, 중보된 요소가 자동으로 제거되도록 
x=[1,2,3,4]
y=[1,2,3]
z= set(x+y)
print(z)
#print(*z)로 출력시 값만 출력됨



#평균을 구하기
print('리스트의 평균:',sum(nuns)//len(nums))
