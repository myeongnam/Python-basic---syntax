# set은 (수학)집합이라고 부르기도 한다.
# set의 특성은 딕셔너리와 마찬가지로, index가 없고 중복이 없다

s1 = {'이름','나이','성별'}
# list의 중복을 제거하기 위해서
# list를 가지고 set 으로 형변환 시키는 방식도 많이 사용
s1 = set(['이름','이름','나이','성별'])

# 집합의 개수 구하는 함수 : len
print(len(s1))
print(s1)

s2 = set('test')
print(s2)

# 인덱스로 접근은 불가
# print(s1[0])

lista = ['A','B','A','AB','O','A']
# 이 반 학생들의 혈액형 종류는 총 몇개인가?
# A,B, AB -> 3개
setA= set(lista)  # 중복을 빼는 식
print(setA)
print(len(setA))   # 갯수 구하기

# SetA의 값을 하나씩 출력하려면? setA[0], setA[1] X
for a in setA:
    print(a)


# 합집합
s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8])
# | shift 원달러 표시 누르면 뜸, 이 기호는 or(또는)를 의미 in 프로그래밍
# s3 = s1 | s2
s3= s1.union(s2)
print(s3)

# 프로그래밍에서 &은 일반적으로 and(그리고)를 의미
# 엠퍼샌드 라고 부른다.
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)


# -,difference 차집합
s3 = s1 - s2
s3 = s2.difference(s1)
print(s3)


# 집합에서 값 추가 : add
s1 = {1,2,3,4,5,6}
# 7을 추가한 다음에 s1 출력
s1.add(7)
print(s1)

# 값 여러개 추가시 update함수(딕셔너리와 동일)
# s1
# s2
# s1에 s2를 update
# s1 출력
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,4,9}
s1.update(s2)
print(s1)


# set값 삭제시 remove,discard 함수 사용
s1 = {1,2,3,4,5,6}
# discard : remove와의 차이점은 
# 삭제할 값이 존재하지않아도 에러가 발생하지 않는다는 점
s1.remove(6)
s1.discard(5)
print(s1)

# boolean (불형)타입
# in ,not in : in(또는 not in) 뒤애 iterable 한 자료형이 나온다
# a in lista, a not in lista, a in dicta, a in seta

# 비어있는 값들은 거짓, 값이 들어있으면 참
lista = [1,2,3]
while lista:
  print('참입니다.')
  lista.pop()
 
#  while 조건: 
#    실행문 

# for 변수 리스트:
#   실행문

