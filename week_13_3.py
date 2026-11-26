#별 표현식
a, b, *c = (0, 1, 2, 3, 4, 5)
print('a:',a,'b:',b,'c:',c)


#딕셔너리
a={}
b=set()#집합

#딕셔너리 key :value
#추가 ->dic이름['key']=value
'''ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)'''

#key에 해당하는 value를 찾는다
'''print(ice['key'])'''

#딕셔너리 요소 삭제 del
'''del ice["메로나"]
print(ice)'''

#닥셔너리 인덱싱
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
print('메로나 가격:',inventory['메로나'][0])#가격
print('메로나 재고:',inventory['메로나'][1])#재고 

#딕셔너리 keys()->키에 집합 
print(inventory.keys()) #리스트로 변환하려면 리스트로 형변환 

#딕셔너리 values()->value의 집합
print(inventori.vslues())

#딕셔너리에 다른 딕셔너리를 추가할때 update
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
