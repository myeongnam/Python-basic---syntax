# 특정한 input값이 있을떄
# 해당 값을 복잡한 로직을 통해서 연산을 한다고 가정하자.
# 그런데 해당 연산은 매우 빈번하게 사용이 된다고 가정하자.
# a=100
# result = (((a+10)*20)/10)**2
# b=200
# result2 = (((b+10)*20)/10)**2
# print(result)
# 복잡한 로직의 연산을 함수화 시켜서 재사용할수 있게 해보자.
# input 값이 있어도 되고, 없어도 된다.
# return값이 있어도 되고, 없어도 된다.


# def myFunc(myInput):
#     calc = (((myInput+10)*20)/10)**2
#     return calc
# # 정의된 함수를 호출할때에는 함수명(input)의 형태로 호출하게 된다.
# result1 = myFunc(100)
# result2 = myFunc(50)
# result3 = myFunc(700)
# result4 = myFunc(115)
# result5 = myFunc(10)

# 함수 직접 구현해보기.
# 함수명은 myPlusFunc 
# 함수의 로직은 사용자의 input을 받아 input 값의 누적합을 더하는
# # 예를 들어 100을 입력하면 1+2+3+....+100

# def myPlusFunc(myInput):
#     totalNum = 0 
#     for a in range(1, myInput+1):
#         totalNum += a
#     return totalNum
# result1 = myPlusFunc(10)
# result2 = myPlusFunc(15)
# print(result1)
# print(result2)

# # input값을 2개를 받아 두 값을 더한뒤, *2만큼 하여 Return하는 함수를 만들어보자
# # 그리고 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자
# def mymy(input1,input2):
#     totalnum = (input1+input2)*2
#     return totalnum

# result = mymy(1,2)
# result1 = mymy(5,5)
# print(result1)


# list의 index 함수를 for문 또는 while문을 통해 
# 9가 몇번째 인덱스에 있는 값인지
# print 해보자
# lista = [1,4,6,9]
# # # print(lista.index(9))
# for a in range(len(lista)):
# #     if lista[a] == 9:
# #         print(a)
# #         break

# # 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다
# # input 값이 2개, print는 함수내에서 하지않고 return에 값을 담는다.
# def myIndex(i1,i2):
#     result = -1
#     for a in range(len(i1)):
#         if lista[a] == i2: 
#             result = a
#             break
#     return result

# lista = [1,4,6,9]
# r1 = myIndex(lista,4)
# print(r1)

# # 원의 넓이를 구하는 함수만들기 
# def circlesize(myinput):
#     result = myinput**2*3.14
#     return result
# # num1 = int(input("반지름의 길이를 입력하세요"))
# # result = circlesize(num1)
# # print("원의 넓이:"+ str(result))

# # # Hello 출력 (입력값이 없는 함수)
# # def hello1():
# #     print("hello1 python")


# # def hello2():
# #     result = "hello2 python"
# #     return result

# # hello1()
# # print(hello2())


# # 입력값의 갯수가 정해져 있지않고 multiple한 함수
# def sum(*args):
#     total = 0
#     for a in args:
#         total += a
#     return total

# totalValue = sum(1,2,3,4,5)
# print(totalValue)

# # 2개이상의 리턴값이 있는 경우 : 튜플 형태로 데이터 return
# def cal(a,b):
#     result1 = a+b
#     result2 = a-b
#     result3 = a*b
#     return result1, result2, result3
# calValue = cal(1,2)

# # 계산한 첫번쨰 결과값은 xx, 두번째 결과값은 yy, 세번쨰 결과값은 zz
# print(f'계산한 첫번쨰 결과값은 {calValue[0]}, 두번째 결과값{calValue[1]}, 세번쨰 결과값{calValue[2]}')

# # 함수에서 default 값 미리 세팅
# def cal(a,b,c='plus'):
#     if c=='plus':
#         result = a+b
#     elif c=='minus':
#         result = a-b
#     elif c == 'multiply':
#         result = a*b
#     return result

# print(cal(1,2))
# # 더한값 출력
# print(cal(1,2,'plus'))
# # 마이너스한 값 출력
# print(cal(1,2,'minus'))
# # 곱한 값 출력
# print(cal(1,2,'multiply'))



# # 매개변수의 순서를 안맞추고도 원하는 매개변수의 자리에 값을 넣어 함수를 호출하는 방법
# def whoAreYou(name, age, gender):
#     print(f"제 이름은 {name}이고, 나이는 {age}, 성별은 {gender}입니다")
# whoAreYou(age=19, name= '홍길동', gender= '남자')


# # 파이썬에서 default값 세팅하는 대표적인 예시가 print 함수
# # print 2개를 사용해서 줄바꿈 없이 hello world 라고 출력이 되도록 만들어보자
# print('hello', end='')
# print(' world')


# # 지역변수와 전역변수
# # 지역변수 : 함수내에서의 변수, 함수내에서만 유효
# # 전역변수 : 함수밖에서의 변수, 함수내에서도 인식가능
# a = 100
# def sum(a,b):
#     # 여기서 a의 값은 100인가? 10인가?
#     # 전역변수인 a=100보다, 함수내에서 선언한 a=10 우선적으로 인식
#     result = a+b
# #     return result
# # result = sum(10,20)
# # print(result) # 함수내의 result라는 변수는 함수밖에서 인식불가
# # #우리가 result 프린트 할수 있었던 것은, 함수내에서 어떤값을 return을 해줬기 때문
# # print(a)


# # for문마다 같은 변수를 사용하는것은 전역변수이기는 하지만,
# # 재할당을 해서 사용하는 것으므로 어차피 reset 되서 문제되지 않는다.
# lista = [10,20,30,40]
# for a in range(len(lista)):
#     print(a)
# for a in range(len(lista)):
#     print(a)   
# print(a)

# # 이중 for문을 사용할때는 문제가 될 여지가 있다
# # 다중 for문을 쓸때는 상위의 for문의 변수를 잃어 버리게 되므로, 다른 변수명 사용.
# for a in range(len(lista)):
#     for a in range(len(lista)):
#      print(a)   
#      print(b)


# 함수내에서 전역변수에 영향을 끼치는 방법 : global
# # 기본적으로 함수내에서 함수밖의 전역변수를 수정할수 없다.
# # 그 이유는 저장되는 메모리 위치가 다르기 때문에.
# result = 0
# def sum(a):
#     global result
#     result += a
#     return result
# value = sum(10)
# print(value)

# 객체는 힙메모리 영역에 저장되는데, 함수내에서도 접슨하여 추가/수정이 가능하다.
# # 스택영역에 있는 지역변수는 함수가 끝나면 휘발되자만 , 힙메모리는 휘발되지 않는다.
# lista = [2,3,4]
# def appendTest(input1, input2):
#     input1.append(input2)

# appendTest(lista,5)
# print(lista)

# 만약에 지역변수가 함수호출이 끝난뒤에도 남아있다면 어떻게 될까?
# 함수에서 사용하는 지역변수가 계속 메모리에 남아있으면,
# 메모리 낭비 뿐만 아니라, 다른 함수에서 해당 변수명을 사용할수 없는 불편함
# def test1(result):
#     result += 10
#     return result
# def test2():
#     result += 100
#     return result

# a = test1(20)
# b = test2()    # This is error code



# # 아래 선택정렬을 함수화 시켜서 활용해보기
def mySort(lista):
    for a in range(len(lista)-1):   # 마지막자리까지 비교할 필요가 없어 -1
        # 두번째 for문은 비교의 대상이 되는 index를 의미
        for b in range(a+1,len(lista)): # 자기자신까지 비교할 필요 없어 +1
            if lista[a] > lista[b]:
            #
                temp= lista[a]
                lista[a] = lista[b]
                lista[b] = temp

lst = [5,1,23,1,6,7,81,2,3,1]
# lst.sort()
# list.sort(lst)
mySort(lst)
print(lst)



# lista에 listb를 담으면 객체의 주소가 복사가 되게 된다
# 그래서 listb가 lista와 동일한 주소, 동일한 데이터를 갖게된다.
lista = [5,1,2]
listb = lista
# 주소 출력하는 함수 : id
print(id(lista))
print(id(listb))
# lista와 값은 갖되, 동일한 메모리 주소가 아니게 할당하고 싶으면 copy함수 사용
import copy
listb = copy.copy(lista)
print(id(listb))
print(listb)