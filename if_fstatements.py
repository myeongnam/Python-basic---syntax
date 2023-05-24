# if 문의 기본 문법
# else는  optional 요소.
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
               
# for문의 기본 구조
# for 변수 in 반복가능한 자료형(iterable)
#     실행문
lista = [10,20,30,40,50,60,70,80,90,100]
for a in lista:
    print(a)

# range 문법 : range(x,y) x이상 y미만
for a in range(1,101):   #1부터 100까지 출력
    print(a)

    