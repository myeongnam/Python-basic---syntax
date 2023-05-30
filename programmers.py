# # 배열자르기

# answer = 0
# numbers = [1, 2, 3, 4, 5]
# num1 = 1
# num2 = 3

# answer = numbers - num1 - num2
# # [2, 3, 4]
# print(answer)


# 문자열 뒤집기 풀이법 3개
# 1번 list로 변환후 reverse로 
# def solution(my_string):
#     stlist = list(my_string)
#     stlist.reverse()
#     answer = "".join(stlist)
#     return answer

# # 2번 슬라이싱
# def solution(my_string):
#     answer = my_string[::-1]
#     return answer

# 3번 : reversed(문자열)
# answer = "",join (reversed(my_string))
# print(answer)

# #배열 원소 길이

# def solution(strlist):
#     answer = []
#     for a in strlist:
#         answer.append(len(a))
#     return answer

#홀수 짝수 개수 구하기

# def solution(num_list):
    
#     num1 = 0
#     num2 = 0
#     for a in num_list:
#         if a % 2 == 0:
#              num1 = num1+1
#         else:
#             num2 = num2+ 1
#     answer = [num1,num2]
#     return answer


# numbers = [1, 2, 3, 4, 5]
# for a in numbers:
#     print(a*2)

# 완주하지 못한 선수
#과부하걸림
# participant = ["leo","leo", "kiki", "eden"]
# completion = ["eden", "leo","kiki"]
# for p in participant:
#     if p in  completion:
#         completion.remove(p)
#     else:
#         print(p)

# # 완주하지 못한 선수
# completion를 dict 로 변환삼h
# # participant 를 for 문으로 1개씩 꺼내서 completion[p]= completion[p]-1

#  participant = ["leo","leo", "kiki", "eden"]
#  completion = ["eden", "leo","kiki"]

# dictc = {}
#  for c in participant:
#   if c not in dictc.keys():
#        dictc[c] = 1
#   else:
#     dictc[c] = dictc[c]+1

# for p in participant:
#   if p in dictc and dictc[p]>0:
#     dictc[p]= dictc[p]-1
#   else:
#     answer = p
  
# # 개미군단
# hp = int()
# for a in hp:
#     a / 5 



# lista = ["1","2","3","4","1","1","3"]
# counta = lista.count("1")
# print(counta)

# 7의 갯수
# array = [7, 77, 17]
# answer = 0
# #문자를 변환해서 쪼개서
# for a in array:
#     b = str(a)
#     answer += b.count("7")

# print(answer)

# # counta = a.count("7")
    


# 카카오톡 문제 확인 
# while True:
#      listSize = int(input("리스트의 크기를 입력해주세요"))
#      if listSize >10:
#           print("다시입력해주세요")
#           continue
#      a=0
#      lista = []
#      while a < listSize:
#       listValue = input("리스트 값을 입력해주세요")
#       lista.append(listValue)
#       a+=1
#      print(lista)



# # 행렬의 덧셈 - 프래그래머스
# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# answer = 0
# # for a in range(len(arr1)):
# #     temp= []
# #     for b in range(len(arr1[0])):
# #         temp.append(arr1[a][b]+arr2[a][b])
# #     answer.append(temp)
# # anwser = [[4,6],[7,9]]




# # price = 150000
# # for a in price:
# #     if a >= 100000:
# #         print(a-a*0.05)
# #     if a >= 300000:
# #         print(a-a*0.1)
# #     if a >= 500000:
# #         print(a-a*0.2)


# def myPlusFunc(myInput):
#     totalNum = 0 
#     for a in range(1, myInput+1):
#         totalNum += a
#     return totalNum
# result1 = myPlusFunc(20)
# result2 = myPlusFunc(40)
# print(result1)
# print(result2)



# lista = [1,4,6,9]
# # print(lista.index(9))
# for a in range(len(lista)):
#     if lista[a] == 9:
#         print(a)
#         break

# for a in range(len(lista)):
#      if lista[a] == 9:
#             print(a)
#             break




def myIndex(i1,i2):
    result = -1
    for a in range(len(i1)):
        if lista[a] == i2: 
            result = a
      
        return 
        break
    return result