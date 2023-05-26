# while 문의 기본구조
# while 조건식: 조건식이 참인 경우 반복 => 무한반복이 기본전제
#      실행문


# 조건을 체크후 True이면 실행문을 1회 실행시키고,
# 다시 조건을 체크하러 돌아온다. 그리고 True 이면 또 다시 실행.
# 그러다, 조건이 False 되면 while 문 종료

# a = 0
# while a<5:
#     print(str(a)+'번 반복')
#     a += 1

# # 1~1000까지만 프린트 되도록 출력.
# a = 1
# while a<1001:
#     print((a))
#     a += 1

# # 1~1000까지 모두 더한 값 출력.
# a = 1
# sum = 0
# while a<=1000:
#     sum += a
#     a += 1
# print(sum)   

# # 평균값
# a = 1
# sum = 0
# while a<=1000:
#     sum += a
#     a += 1
# print(sum/1000) 



# While 문에서 반복을 진행하다가 break를 만나면, 반복문 종료.
# # 1) if 문을 써서 xxx 한 조건에 break
# a = 1
# sum = 0
# while True:
#     sum += a
#     if a==1000:  # a가 1000이면 break
#         break
#     a += 1
# print(sum)

# countinue :  이 구문을 만나면, 다시 반복문 조건으로 이동.
# 하단에 불필요한 로직을 수행하지않고 다시 조건으로 이동할수 있게 해준다.
# # 아래와 같이 코딩하면 hello가 무한 출력
# a =  0
# while a<1000:
#    print("hello")
#    continue
#       a+=1



# 2) 1~1000충에 홀수만 더해서 출력

# a = 0
# sum = 0
# while a<1000:
#     a += 1
#     if a % 2 !=0:
#       sum += a
# print(sum)    


 # [::2] 이걸 써서 못푸나?
# new_list = list(range(1,1001))[::2]
# print(sum(new_list))



# a = 0
# sum = 0
# while a<1000:
#      a += 1
#      if a % 2 ==0:
#         continue
#      sum +=a
#        # continue를 활용해서 coding
# print(sum)  

# 로또 번호 생성기
# 랜덤의 값을 추출하는 파이썬 라이브러리 -> random

import random  # 이걸 꼭 해줘야함!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(random.randint(1,45))
# 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자.
a = 0
lista = []
while a < 6:
 randnum = random.randint(1,45)
 lista.append(randnum)
 a+= 1
print(lista)








# for문의 기본 구조
# for 변수 in 반복가능한 자료형(iterable)
# #     실행문
# lista = [10,20,30,40,50,60,70,80,90,100]
# for a in lista:
#     print(a)

# # range 문법 : range(x,y) x이상 y미만
# for a in range(1,101):   #1부터 100까지 출력
#     print(a)


# range의 의미 : iterable 객체
v1 = list(range(1,10))   # 1~9까지 출력
print(v1)
# for a in range(1,101):   #1부터 100까지 출력
#     print(a)

# range(x,y) : x 이상 y 미만의 숫자를 담은 객체
# range(y) : 0이상 y미만의 숫자를 담은 객체


v1 = list(range(10,20))

# for a in 리스트
for a in v1:
 print(a) 

# for a in range 를 써서 v1[index]의 형태로 v1의 값을 모두 출력
for b in range(len(v1)):
 print(v1[b])

 # for a in 리스트 구문으로는 원본리스트 데이터를 변경할수 없다.
 lista = [10,20,30,40,50,60,70,8,90,100]
 for a in lista:
  a = 100 # 이런 방식으로는 원본의 lista 의 값을 변경할수 없다


# 직접 리스트의 index로 접근해야지 원본을 바꿀수 있다 .
  for a in range(len(lista)):
   lista[a] = 100

   print(lista)


   # 리스트를 만드는 방법중에 리스트 컴프리헨션이라는 방법이 있다
# 리스트에 0~9까지를 담는 방법
# 방법1
lista = [0,1,2,3,4,5,6,7,8,9]
# 방법2
lista = list(range(10))
# 방법 3
lista = []
for a in range(10):
 lista.append(a)
# 방법 4 : 리스트컴프리핸션
lista = [a for a in range(10)]
print(lista)

