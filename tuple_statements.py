# tuple은 변경불가능한 자료형으로서, ()소괄호를 통해 표현
# t1 = (1,2,'a','b')
# print(t1)
# # 인덱싱, 슬라이싱 둘다 리스트와 동일하게 허용
# print(t1[0])


# # 삭제,변경 불가
# del t1[0]
# print(t1)

# 튜플을 사용하는 이유는 개발자가 해당 자료를 수정하지 못하도록 
# 강제적으로 지정한것.
paymethod = ('cash','card','tmoney')
p1 = input("어떤 방법으로 결제 하시겠습니까?")
if p1 not in paymethod:
     print ("사용하실수 없는 결제 방법입니다.")