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


participant = ["leo","leo", "kiki", "eden"]
completion = ["eden", "leo","kiki"]
for p in participant:
    if p in  completion:
        completion.remove(p)
    else:
        print(p)