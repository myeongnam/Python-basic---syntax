# flie 시스템 입출력 라이브러리 : open
# open 함수는 mode(w,r,a)을 갖고 있다.
# # w : write(덮어쓰기), r:read, a: 추가
# # # open을 했을때 해당 파일명이 없으면 자동생성
# # f = open("test.txt",'w')
# # f.close()

# f = open("test.txt","w", encoding= "UTF-8")
# for i in range(0,10):
#     data = "%d 번째 줄입니다.\n" %i
#     f.write(data)
# f.close() 



# f = open("test.txt","r", encoding= "UTF-8")
# # 첫번째 줄만 가져오는 함수
# # while, if 문으로 readline올 전체 출력

# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break
# f.close()



# f = open("test.txt","r", encoding= "UTF-8")
# # readlines : 데이터를 리스트형태로 라인별로 담아준다
# lines = f.readlines()
# print(lines)


# f = open("test.txt","r", encoding= "UTF-8")
# # read: 데이터를 한꺼번에 문자열 형태로 담아준다
# lines = f.read()
# print(lines)


# a 옵션으로 추가모드
f = open("test.txt","a", encoding= "UTF-8")
# 0~9번째 줄입니다. -> 10~19번째 줄입니다.
for a in range(10,20):
    data = "%d번쨰 줄입니다\n" %a
    f.write(data)
f.close

# 파이썬에서 객체를 생성하고 나면, 힙메모리에 객체 할당된다.
# 객체의 사용이 끝나면 객체를 close 해줘야 하나?
# 그럴 필요가 없는게, 파이썬에는 GC(Garbege Collector)가 내장되어
# 자동으로 사용빈도가 낮은 데이터는 메모리에서 삭제를 해준다
# 그러나 파일시스템은 그렇지 못하므로 직접 닫아줘야한다
# 그래야 메모리 낭비가 없다.

import os
# # # os 라이브러리를 활용한 디렉터리 내에 파일 검색.
# searchDir = r'C:\Users\User\Desktop\김명남'
# # 파일, 디렉토리 목록을 뽑아내는 listdir 함수사용
# dirList = os.listdir(searchDir)
# for dir in dirList:
#     dirTuple = os.path.splitext(dir)
#     if(dirTuple[1]=='.py'):
#         fullPath = os.path.join(searchDir, dir)
#         print(fullPath)

# # 그 다음 폴더까지 검색
# searchDir = r'C:\Users\User\Desktop\김명남'
# dirList = os.listdir(searchDir)
# for dir in dirList:
#     filename  = os.path.join(searchDir,dir)
#     if os.path.isdir(filename):
#         dirList2 = os.listdir(filename)
#         for dir2 in dirList2:
#             dirTuple2 = os.path.splitext(dir2)
#             if(dirTuple[1]=='.py'):
#                 fullPath = os.path.join(searchDir, dir)
#             print(fullPath)
#     dirTuple = os.path.splitext(dir)
#     if(dirTuple[1]=='.py'):
#             fullPath = os.path.join(searchDir, dir)
#             print(fullPath)


# 모든 폴더까지 검색
def searchRecur(searchDir):
    try:
        dirList = os.listdir(searchDir)
        if not dirList:
            return  # 함수를 종료시킨다는 의미
        for dir in dirList:
            filename  = os.path.join(searchDir,dir)
            if os.path.isdir(filename):
                searchRecur(filename)
            dirTuple = os.path.splitext(dir)
            if(dirTuple[1]=='.py'):
                fullPath = os.path.join(searchDir, dir)
                print(fullPath)
    except Exception:
        print('예외입니다')
searchDir = r'C:\Users\User\Desktop\김명남'
searchRecur(searchDir)