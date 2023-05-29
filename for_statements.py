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

# import random  # 이걸 꼭 해줘야함!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # print(random.randint(1,45))
# # 리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만들어보자.
# a = 0
# lista = []
# while a < 6:
#  randnum = random.randint(1,45)
#  lista.append(randnum)
#  a+= 1
# print(lista)








# for문의 기본 구조
# for 변수 in 반복가능한 자료형(iterable)
# #     실행문
# lista = [10,20,30,40,50,60,70,80,90,100]
# for a in lista:
#     print(a)

# # range 문법 : range(x,y) x이상 y미만
# for a in range(1,101):   #1부터 100까지 출력
#     print(a)


# # range의 의미 : iterable 객체
# v1 = list(range(1,10))   # 1~9까지 출력
# print(v1)
# # for a in range(1,101):   #1부터 100까지 출력
# #     print(a)

# # range(x,y) : x 이상 y 미만의 숫자를 담은 객체
# range(y) : 0이상 y미만의 숫자를 담은 객체


# v1 = list(range(10,20))

# # for a in 리스트
# for a in v1:
#  print(a) 

# # for a in range 를 써서 v1[index]의 형태로 v1의 값을 모두 출력
# for b in range(len(v1)):
#  print(v1[b])

#  # for a in 리스트 구문으로는 원본리스트 데이터를 변경할수 없다.
#  lista = [10,20,30,40,50,60,70,8,90,100]
#  for a in lista:
#   a = 100 # 이런 방식으로는 원본의 lista 의 값을 변경할수 없다


# # 직접 리스트의 index로 접근해야지 원본을 바꿀수 있다 .
#   for a in range(len(lista)):
#    lista[a] = 100
#    print(lista)


#    # 리스트를 만드는 방법중에 리스트 컴프리헨션이라는 방법이 있다
# # 리스트에 0~9까지를 담는 방법
# # 방법1
# lista = [0,1,2,3,4,5,6,7,8,9]
# # 방법2
# lista = list(range(10))
# # 방법 3 : 홀수인 값에 2를 곱한 값만을 list로 만들어라
# lista = []
# for a in range(10):
#  if a % 2 !=0:
#   lista.append(a*2)
# # 방법 4 : 리스트컴프리핸션
# # 장점 : 간결하다

# lista = [a*2 for a in range(10) if a % 2 !=0]
# print(lista)




# 1반에 수학 점수가 60점이 넘으면 합격, 60 미만이면 불합격.
# lista = [90,25,67,45,80]
# 위 list가 학생의 번호 순서대로 있을때, 아래와 같이 출력하도록 코딩하여라.
# 1번 학생은 불합격입니다.
# 2번 학생은 합격입니다.

# 방법1
# lista = [90,25,67,45,80]
# num = 1 
# for a in lista:
#     if a >= 60:
#       print('%d번 학생은 합격입니다.' %num)
#     else:
#       print('%d번 학생은 불합격입니다'%num)
#     num += 1

# 방법2
# lista = [90,25,67,45,80]

# for a in range(len(lista)):
#     if lista[a] >= 60:
#       print('%d번 학생은 합격입니다.'% (a+1))
#     else:
#       print('%d번 학생은 불합격입니다'% (a+1))


# for 문과 break : for 문에서 break문을 반드시 써야 하는 상항
# # 혈액형이 a형인 고객 선착순 1명만 찾는 상황
# lista = ['b','b','ab','a','b','a']
# for a in range(len(lista)):
#   if lista[a] =='a':
#    answer = a+1
#   # break를 넣고 안넎고 결과값 차이
#    break
# print(str(answer) + "번쨰 고객이 이벤트에 당첨돠었습니다")


#for문을 이용한 구구단
# 구구단 5단을 출력해보자
# 5X1 = 5
# # 5x2 = 10
# for a in range(1,10):
#   print(f"5 X {a} = {5*a}")



# # 구구단 몇단을 계산해드릴까요?
# num = int(input("구구단 몇단을 계산해드릴까요?"))
# for a in range(1,10):
#    print(f"{num} X {a} = {num*a}")

# 2중 for문
# 구구단을 5단~9단까지 한꺼번에 출력

# num = 5
# while num <10:
#    for a in range(1,10):
#       print(f"{num} X {a} = {num*a}")
#    num += 1

# for num in range(5,10):
#    for a in range(1,10):
#       print(f"{num} X {a} = {num*a}")



# lista = [10,20,30,40]
# # lista[0]과 lista[1]의 자리를 바꿔라
# # 결과값[20,10,30,40]
# temp = lista[0]
# lista[0] = lista[1]
# lista[1] = temp

# python에서 지원하고 있는 문법
# lista[0],lista[1] = lista[1], lista[0]
# print(lista)

# for 문을 이용한 정렬 알고리즘
lista = [93,45,21,30,20,94,66,71,45]

# 위 리스트를 어떻게 오름차순 정렬 할 것인가?
# lista.sort()
# print(lista)
# 파이썬제공 기본 함수 lista[a],lista[b] = lista[b], lista[a]

# 선택정렬 : 0번째 index부터 가장 작은 값을 채워나가는 방식
# 첫번째 for문은 채워나가야할 index를 의미
for a in range(len(lista)-1):   # 마지막자리까지 비교할 필요가 없어 -1
    # 두번째 for문은 비교의 대상이 되는 index를 의미
    for b in range(a+1,len(lista)): # 자기자신까지 비교할 필요 없어 +1
        if lista[a] > lista[b]:
           # 자리 change
            temp= lista[a]
            lista[a] = lista[b]
            lista[b] = temp

print(lista)
# 버블정렬
lista.sort()
