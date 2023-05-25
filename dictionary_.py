
# # 딕셔너리 자료형은 key와 value로 이루어져있다.
# # 영어사전에서 단어와 뜻으로 이루어져있던것에서 유래.
# dic1 = {'이름': '홍길동', '나이':25, '성별': '남'}


# # 파이썬에서의 dictionary는 
# # 다른 lanugage의 map 또는 hashmap과 유사한 자료형
# # json 이라는 자료형태와도 유사하다.

# # 딕셔너리의 특징1  {} 중괄호 사용
# # key는 중복이 불가.
# # value는 다른 key에도 존재할수 있다.
# dic1 = {'이름': '홍길동', '나이':25, '성별': '남','성별': '여'}
# print(dic1) # {'이름': '홍길동', '나이': 25, '성별': '여'} 뒤에 key 덮어씀, 일반적으로 중복 불가.


# # 딕셔너리의 기본호출 방식은 변수명[key] 대괄호, 변수명.get(key) - 2가지 방법
# print(dic1['나이'])
# print(dic1.get('나이'))

# # 리스트는 a = [value,...]
# # 딕셔너리는 a = {key: value}
# # 튜플은 a = (value,...)

# # 리스트와 튜플은 a[index], 딕셔너리는 a[key]

# # 딕셔너리의 특징2
# # key와 value로 이루어져 있다보니, 순서는 의미가 없다, index로 접근불가
# # ket를 가지고 value 검색할때 해시함수를 통해 index를 찾다보니, 매우 빠른 속도 보장.

# dic1 = {'이름': '홍길동', '나이':25, '성별': '남','성별': '여'}
# # key: value 추가
# dic1 ['신분'] = '학생'
# print(dic1)

# # {'이름': '홍길동', '나이': 25, '성별': '여', '신분': '학생'}

# # 딕셔너리에서 키를 이용한 key:value 삭제
# del dic1['성별']
# print(dic1)
# # {'이름': '홍길동', '나이': 25, '신분': '학생'}


# # 딕셔너리에서 key 목록만 뽑아낼때
# # iterable 한 형태로 data가 뽑아져 나오므로 for문 사용가능.
# keylist= dic1.keys()
# print(keylist)


# # 위의 keylist 에서 각각의 값을 출력해보자
# for k in keylist:
#     print(k)
# # 이름
# # 나이
# # 신분

# # key을 출력해주는 for 문안에서 value도 같이 출력해보자
# print(dic1[k])

# # 위의 for문을 활용해서, key가 담긴 list 를 만들고, value가 담긴 list를 만들어 각각출력 해보자
# templist1 = []
# templist2 = []
# for k in keylist:
#     templist1.append(k)
#     templist2.append(dic1[k])
# print(templist1)
# print(templist2)   



# # value 목록을 뽑아낼떄는 .values() 사용
# valueList = dic1.values()
# for v in valueList:
#     print(v)

# dict_values(['홍길동', 25, '학생'])

# 딕셔너리의 확장 : update함수
# dic1 = {"a":1,"b":2, "c":3}
# dic2 = {"a":2,"d":4,"f":5}
# dic1.update(dic2)
# print(dic1)

lista = ['a','a','b','ab','o','ab','o']
dicta = {'a':2, "b":2, "o":2}
# 딕셔너리로 변환해서 출력해보자.
# 예를 들어 'a':2,'b':1,'o':2 이렇게 출력되도록 코딩해보자
# hint : a in dicta.keys() 을 통해 a키가 dicta 에 이미 있는지
# 검사
dicta = {}
for a in lista:
  if a not in dicta.keys():
   dicta[a] = 1  
  else:
    dicta[a] = dicta[a] +1
print(dicta)     #{'a': 2, 'b': 1, 'ab': 2, 'o': 2}

dicta = {}
for a in lista:
 if a not in  dicta.keys():
  dicta[a] = lista.count(a)
print(dicta)