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



def myIndex(i1,i2):
 for a in range(len(lista)):
    if lista[a] == 9:
        print(a)
        break

lista = [1,4,6,9]
r1 = myIndex(lista,4)
print(r1)
