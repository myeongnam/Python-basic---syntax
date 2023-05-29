# # a = 10
# # if (a>5) | (a>100):
# #     print('참입니다1')
# # if a>5 or a > 100 :
# #     print('참입니다2') 

# # 비트연산이란 2진법의 숫자를 |(or), &(and) ,^(xor)등으로 
# # CPU 내부적으로 계산하는 방식
# # ex)
# # 1111 and 1000 => 1000
# # 1111 or 1000 => 1111

# # and는 & 와 같고, or은 | 와 같고, not 은 부정의 의미
# # not True는 False가 되고, not False는  True가 된다.


# # 대입연산자
# a = 10 
# # a = a+1 이렇게 표현해도 되고, a+= 1 이렇게 표현 가능.
# a += 1
# print(a)

# # -=,/=,*=
# # a/=5 => a = 2 = a/5
# print(a/5)

# # 비교연산잔 중에 chaining 
# # 5<a<100 이렇게 표현하거나 a>5 and 100<a
# a = 10
# if a > 5 and 100 < a:
#     print("참입니다")




# if 문의 기본 문법
# else는  optional 요소.
# else상단에 있는 if 또는 elif에 종속된다
# elif도 마찬가지로 elif 상단에 if 에 종속된다.
# 90이하면 예각입니다. 를 출력
# 90이면 직각
# 91~179면 둔각
# # 180이면 평행
# # ~~중 하나만을 실행시키고자 할떄는 elif를 if에 종속시켜 실행하면 실수가 없다.
# num1 = int(input("숫자를 입력해주세요"))
# if num1 < 90:
#     print('예각입니다.')
# elif num1 ==90:
#     print("직각입니다")
# elif num1 < 180:
#     print("둔각입니다")
# elif num1 ==180: #else를 써도 되고, 안써도 된다
#     print("직각입니다")



# if 참조건:
#      실행문
# else:
#     실행문

# a = int(input("숫자를 입력해주세요"))
# if a>10:
#     print("a는 10보다 큽니다")
# else:
#     print("a는 10보다 작습니다")

# trueorfalse = True
# if trueOrFalse:
#     print("참입니다")
# else:
#     print("거짓입니다")


# 얼마를 가지고 있습니까?를 변수에 담고
# 만약 30,000 이상이 있으면, 택시를 타고 가시오를 출력
# 그렇지않으면 걸어가시오를 출력

# a = int(input("얼마를 가지고 있습니까")) 
# if a > 30000:                           
#     print("택시를 타세요")                  
# else:
#     print("걸어가세요")
               
# a = 10
# if a>5:
#     print("참입니다")
# if a>100:
#     print("참입니다")
# else:
#     print("거짓입니다")


# if 문 한줄로 쓰기
# 코드가 짧고 단순한 경우에 아래와같이 한줄로 쓰는것을 권장
# 두 줄이상의 코드를 한줄로 적고싶으면 ;으로 구분
# a = 10
# if a>1: print("a는 1보다 큽니다");print("a는 1보다 큽니다")

# # 조건부표현식(삼항연산자) : 간단한 식으로 표현
# # 먼저 if문의 실행문을 if 문 앞으로 ,: 빼고, 한줄로
# a = 10
# print('A는 10보다 큽니 다')if a>10 else  print('A는 10보다 작습니다')

# 실행문을 실행하기 위해 사용한다기보다는
# 참인 경우에 어떤값, 거짓인 경우에 어떤값을 쉽게 result에 담기
# a=10
# result = 'A는 10보다큼' if a>10 else 'A는 10보다 작음'
# if a>10:
#     result = 'A는 10보다 큼'
# else:
#     result = 'A는 10보다 작음'
# print(result)


# lista = [1,2,3,4,5,6,7]
# a = int(input("숫자를 입력하세요"))
# if a in lista:
#     print("입력하신값이 목록에 있다")
# else:
#     print('없습니다')


a = int(input("짐은 무게는 얼마입니까?"))
weight = (a // 10) * 10000
print("짐의 무게는 %d 이고 수수료는 %d 입니다 "%(a, weight))
# f formating
print(f"짐의 무게는{a} 이고 수수료는 {weight} 입니다")


# money = int(input("얼마를 가지고 있습니까?"))
# hungrtornot = input('배가 고프신가요 yes or no 로 대답해주세요')
# if money > 10000 and hungrtornot =='yes':
#     print("밥을 사먹으시오")
# else:
#     print("집에가세요")

# a 와 b 같은지 비교하는 연산자 is
# 객체타입으이 경우에는 메모리 주소를 비교하고
# 숫자, 문자, bool 기본타입의 경우 값을 비교한다.
# 숫자, 문자, bool같은 경우에는 데이터 pool을 만들어서 재활용한다
# 그래서 값을 비교할때 메모리 주소가 아니라, 데이터 pool에서 값을 직접 비교
a = 10
b = 10
if a is b:
    print("참입니다")

a = 10 
b = 10
if a == b:
    #pass시키는것.(pass를 명시적으로 표현한것)
    pass
else:
    print('두 값이 다릅니다')

