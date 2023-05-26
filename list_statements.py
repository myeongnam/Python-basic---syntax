# # list는 변수마다 값을 할당해서 사용하기에, 관리의 어려움이 있으므로 
# # 한 변수에 값을 집합시켜놓은 것

# # a = "김감감"
# # b = "김갑돌"
# # c = "김갑순"
# # print(a)



# # 하나의 변수로 여러개의 데이터를 관리
# # # list의 경우 [] 대괄호를 사용하여 데이터를 집합
# # lista = [김감감", "김갑돌", "김갑순']

# # #  # list 안의 각각의 값에 접근할때에는 index 사용
# # #  print(lista[0])
# # #  print(lista[1])
# # #  print(lista[2])

# #  # 여러개의 데이터를 범위를 지정해서 가져오고 싶을때는 slicing사용
# #  # 슬라이싱의 결과값은 같은 list로 출력
# #  # 0~5번째까지 출력

# # print(lista[0:5]) 

# #  # 0~5번째까지 출력한 결과물의 type 출력
# # print(type(lista[:5]))

# # 문자열은 메모리 내부적으로 list와 유사한 자료구조
# # 문자열은 값을 추가하거나 수정할수가 없다.
# # list는 값을 추가,삭제,수정이 가능한 구조를 가지고 있다.


# # list_ex1 = ['a','b','c',[1,2,3]]이라는 리스트가 있다
# # # 1) 변수 number에 [1,2,3]을 담아 출력하라
# # # 2) number에 담은 값 중 1과 3을 더해 4를 출력하라
# # list_ex1 = ['a','b','c',[1,2,3]]
# # number = list_ex1[3]
# # print(number[0]+number[2])
# # print(list_ex1[3][0]+list_ex1[3[2]])
      

# # 리스트 더하기 또는 곱하기
# # 리스트를 2개 선언하고 만들어서,
# # 2개를 더해서 하나의 리스트로 만들어보자 그리고 출력
# # lista = [1,2,3]
# # listb = [4,5,6]
# # listc = lista + listb
# # print(listc)
# # print(listc*10)

# # 리스트 길이 구하기 : len
# # print(len(lista))

# # 리스트값 수정하기 
# # -> 1개의 값만 바꿀땐 1개의 값으로 대체
# # -> 여러값을 바꿀땐 다른 리스트로 대체 

# lista = [1,3,5,6,7,9]
# lista[1] = 4 
# print(lista)
# lista[2] =  [5,5,5]
# print(lista)

# # # 리스트 요소 갯수 세기
# # lista = ["1","2","3","4","1","1","3"]
# # counta = lista.count("1")
# # print(counta)


# # # 리스트 요소 삭제하기 : del 변수[인덱스]
# # a = [1,3,5,7,9,10]
# # del a[3]
# # print(a)


# # # 리스트 요소 삭제하기: remove
# # a = [1,3,5,7,9,10]
# # a.remove(1)
# # print(a)


#  # 모든 특정한 9라는 값을 모두 삭제하려면?
#  # del, for range

# # lista = [1,3,9,3,5,6,9,9]
# # 방법1
# # index가 2일때, 9니깐 del => 3
# # # 7을 검사하려고 하니 7이 없네
# # count = 0
# # for a in range(0, len(lista)):
# #   if lista[a-count] == 9:
# #    del lista[a-count]
# #    count = count + 1
# # print(lista)

# # lista = [1,3,9,3,5,6,9,9]
# # listb = []
# # for a in range(0, len(lista)):
# #   if lista[a] != 9:
# #    #listb = listb +[lista[a]]
# #    del lista[a]
# # print(lista)

# # lista = [1,3,9,3,5,6,9,9]
# # for a in range(0, len(lista)):
# #   if 9 in lista:
# #    lista.remove(9)
# #   else:
# #    break
# # print(lista)


# #  list append : 리스트 맨뒤로 추가
# lista = [1,3,5,7]
# # 9,10을 append 이용해서 추가해서 출력
# lista.append(9)
# lista.append(10)
# print(lista)


# #list insert : index를 지정하여 추가 가능
# #lista.index(2,"abc") 추가 후 출력
# lista.insert(2,"abc")
# print(lista)


# # list extend : iterable 객체를 lsit에 추가할때 사용
# # extend는 각 요소를 꺼내어\ 맨 뒤에 추가
# listb = [10,20,30]
# lista.extend(listb)
# print(lista)


# # list의 정렬은 sort ()함수 사용
# # sort()는 오름차순 정렬
# # reverse= True 옵션을 주면 내림차순 정렬
# numa = [3,12,5,6,2,64,]
# numa.sort() # numa.sort(reverse= True)
# print(numa)

# # 
# chlist = ['brad',' john','abc']
# chlist.sort()
# print(chlist)

# #list 뒤집기 : reverse()
# chlist.reverse()
# print(chlist)


# #list 위치반환 : index()
# lista = ["김돌쇠","김갑동", "김갑순", "김철수"]
# print(lista.index("김철수"))


# # 마지막 요소 끄집어 내기 : pop()
# # remove and return last value   Print(lista.pop())
# lista.pop()
# print(lista)


# # 문자 리스트를 문자열로 만들기
# lista = ["hello","worrld","python"]
# st1 = ""
# st2 = st1.join(lista)
# print(st2)


# # 문자열을 문자 리스트로 만들기

# lista = ["hello","worrld","python"]
# sta = "hello world python"
# mysta1 = list(sta)
# mysta2 = sta.split()
# print(mysta2)


# 최대값 구하기,# minimum 구하기

lista = [100,25,30,5,90]
maxa = lista[0]
mina = lista[0]
# 위 리스트의 최대값을 정렬함수x, 최대값함수x, for문 O
for a in lista:
 if maxa < a:
    maxa = a
 if mina > a:
    mina = a 
print(mina)  
print(maxa)

# 방법2. max
maxa = max(lista)
mina = min(lista)

# 방법3. sort
lista.sort()
mina= lista[0]
maxa = lista[len(lista)-1]
maxa = lista[-1]
print(maxa)

if a > 5 | a>100:
  print('참입니다.')
