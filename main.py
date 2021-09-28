# 자료형
print("hello world")

a = 1
print(a)
print(type(a))

a = 3
b = 4

print(a / b)
print(a // b)  # 몫을 출력
print(a % b)

a = "python's favorite  \n food is perl"
b = "python's favorite  \t food is perl"
c = """ python's favorite  
         food is perl"""
print(a)
print(b)
print(c)

# 인덱싱
a = "python's favorite food is perl"
print(a[0])
print(a[-1])
# ==================
# 슬라이싱 [이상:미만:간격]
print(a[3:8])
b = "1234567"
print(b[::3])
# ==================
a = "I eat %d apples." % 3
print(a)
number = 10
day = "three"
a = "I aet %d apples. so I weas sick for %s days." % (number, day)
print(a)

a = "abcde {} sdfsdf".format("안녕")
b = "abide {name} sdfsdf".format(name=" 민경환")
c = "abide {age} sdfsdf{name}".format(name=" 민경환", age=30)
name = "int"
d = f"나의 이름은 {name} 입니다"
print(a)
print(b)
print(c)
print(d)

a = "%0.2f" % 3.431342324
print(a)

a = "hobbby"
print(a.count('b'))
print(a.find('b'))  # 0부터 시작
print(a.index('b'))

a = ",".join("abcd")
print(a)
a = ",".join(["a", "b", "c"])
print(a)

a = " hi "
print(a.upper())
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))
print(a.split())  # 리스트로 반환

# 리스트
a = ["이시영", "문재성", "int", "김정현"]
print(a)
print(a[1])

a = [1, 2, "이시영", "문재성", ["int", "김정현"]]
print(a)
print(a[4])
print(a[4][1])

a = [1, 2, 3, 3, 3, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a[0:3])
print(a + b)
a[0:2] = [10, 20]
print(a)
a[0:2] = []
print(a)
a.append(400)
print(a)
a.sort()
a.reverse()
print(a)
print(a.index(400))
a.insert(1, 500)
print(a)
a.remove(3)
print(a)
print(a.pop())  # 마지막 값 빼내기
a.extend([6, 7])
print(a)

# 4강 자료형2
# 리스트 , 튜플
# a = [1,2,3] a=[8,2,3] 리스트 변경가능
# 튜플 b=(1,2,3) 튜플 변경불가능 (길이,값 고정)

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1[0:2])
print(t1 + t2)
t2 = t2 * 3
print(t2)

# 딕셔너리(사전)
# ex)Json(API)
# 연관 배열 또는 해시
# Key를 통해 Value를 얻는다.

dic = {'name': 'Eric', 'age': 15}
print(dic['name'])

a = {1: 'a'}
a['name'] = "익명"  # 딕셔너리 추가하기
print(a)

del a[1]  # 키 값으로 삭제
print(a)

a = {1: 'a', 1: 'b'}  # 마지막 값이 나옴
print(a)

a = {1: '파랑구름', 2: '이현준', 3: "민경환"}
print(a.keys())
print(a.values())
print(a.items())

for k, v in a.items():
    print("키는 : " + str(k))
    print("벨류는 :" + v)
# a.clear()
# print(a.items())
print(a.get(1))
print(a.get(4))  # None 출력 # print(a[4]) == 에러
print(a.get(4, '없음'))
print(4 in a)  # 키 찾기
print(1 in a)

# 집합
# 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
# 중복을 허용하지 않는다.
# 순서가 없다
s1 = set([1, 2, 3])
s1 = {1, 2, 3}
print(type(s1))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 자바로 하면 이중 for문 돌려야함.
print(s1 & s2)  # s1과 s2의 교집합
print(s1.intersection(s2))  # s1과 s2의 교집합
print(s1 | s2)  # 합 집합
print(s1.union(s2))
print(s1 - s2)  # 차 집합
s1.add(10)
print(s1)
s1.update([11, 12, 13, 1])
print(s1)
s1.remove(1)
print(s1)

# 불 boolean  (문자열,리스트 등)값이 있으면 참, 없으면 거짓
a = True
print(type(a))
a = "안녕"
if a:
    print(a)
a = [1, 2, 3, 4]
while a:
    a.pop()  # 마지막 요소 없애고 출력
    print(a)
############# 변수
# a = 3
# 3이라는 값을 가지는 정수 자료형(객체)이 자동으로 메모리에 생성
# 변수 a는 객체가 저장된 메모리의 위치를 가리키는 레퍼런스(Reference)
# a라는 변수는 3이라는 정수형 객체를 가리키고 있다.
# https://pythontutor.com/live.html#mode=edit
a = [1, 2, 3]
b = a
a[1] = 4
print(id(a))  # id == 주소 값
print(id(b))
print(a is b)  # 같은 주소를 같는지 확인

a = [1, 2, 3]
b = a[:]  # a의 값을 슬라이싱(주소x)
a[1] = 4
print(a)
print(b)
print(id(a))  # id == 주소 값
print(id(b))

from copy import copy  # 값을 복사

a = [1, 2, 3]
b = copy(a)
a[1] = 4
print(a)
print(b)
print(id(a))  # id == 주소 값
print(id(b))
# 튜플을 이용한 변수 값 할당
a, b = ('python', 'life')
(a, b) = 'python', 'life'
# 리스트를 이용한 변수 값 할당
[a, b] = ['python', 'life']
a = b = 'hello'
print(a)
print(b)
# 값 바꿔서 넣기
a = 3
b = 5
a, b = b, a
print(a)
print(b)

################# 5강 (3장)제어문 ##############
# 조건문 , python == 들여 쓰기!
money = True
if money:
    print("택시승차")
else:
    print("걷기")

a = 1
b = 2
if a < b:
    print("참")
else:
    print("거짓")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    pass
elif card:
    print("택시")
else:
    print("걷기")
# 조건부 표현식 (삼항연산자)
score = 80
massage = "sucess" if score >= 60 else "failure"
print(massage)

# while 문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어감")
# break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다.")
        break
# continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

# for 문 (자바의 향상된 for문)
# for 변수 in 리스트(튜플,문자열)
#   수행할 문장
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
    print(first)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격" % number)
    else:
        print("%d번 학생은 불합격" % number)

# range
sum = 0
for i in range(1, 11):  # 1~10
    sum = sum + i
    print(i)
print(sum)

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")  # 붙여서 출력
    print('')


# 리스트 내포
# result = [num *3 for num in a if num % 2 ==0]
# result =[]
# for num in a:
#    if num%2 ==0:
#        result.append(num*3)
# 이중 포문
# result = [x*y for x in range(2,10) for y in range(1,10)]

# result = []
# for x in range(2,10):
#     for y in range(1,10):
#         result.append(x*y)

############### 4장 함수 ####################
# def 함수명(매개변수)
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
#     return 리턴 값
def sum(a, b):
    result = a + b
    return result
print(1+3)

def say():
    return 'H1'
print(say())

def sum(a,b) :
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))
print(sum(1,2))

myList = [1,2,3]
print(myList.append(4)) # 리턴값이 없음.
print(myList.pop()) # 리턴값이 있음.

#입력도 출력도 없는 함수
def say():
    print('HI')
print(say())

def sum_many(*args): # *변수(여러개 값이 들어감) == (a,b,c,d,...)
    sum = 0
    for i in args:
        sum=sum+i
    return sum
print(sum_many(1,2,3))

def print_kwargs(**kwargs): # keyword arguments 딕셔녀리
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은:" +k)
print(print_kwargs(name="1", b="2"))

#함수의 결과 값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b, a*b  #튜플형태

print(sum_and_mul(1,2)[0])
print(sum_and_mul(1,2)[1])

#매개변수에 초기값 미리 설정하기
def say_myself(name,old,man=True):  # 초기값은 맨 마지막에 써줘야함.
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자 입니다.")
say_myself("민경환",20)
say_myself("민경환",20,False)

#함수 안에서 선언된 변수의 효력 범위
a = 1 # 전역 변수
def vartest(a):
    a=a+1 # 지역변수
vartest(a)
print(a)
#함수 안에서 함수 밖의 변수를 변경하는 방법1
a = 1
def vartest(a):
    a=a+1
    return a
a=vartest(a)
print(a)
#함수 안에서 함수 밖의 변수를 변경하는 방법2
a = 1 #전역 변수
def vartest():
    global a #전역 변수
    a=a+1
vartest()
print(a)

#Lambda
#def add(a,b):
#   return a+b
add = lambda a, b: a+b
print(add(1,2))
myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList[0](1,2))

# 사용자 입력과 출력
# a = input()
# print(a)
#
# number = input("숫자를 입력하시오.")
# print(number)
print("life" "is" "too short")
print("life", "is", "too short")
for i in range(10):
    print(i,end=' ') #end를 뒤에 붙인다.

#파일 읽고 쓰기
# f = open("새파일.txt",'w') # r-읽기모드, w-쓰기모드, a-추가모드(파일의 마지막에 새로운 내용 추가)
# f.close()
#
# f = open("새파일.txt","w",encoding="UTF-8")
# for i in range(1,11):
#     data = "%d번째 줄입니다. \n" % i
#     f.write(data)
# f.close()

#readline()함수
# f=open("새파일.txt",'r',encoding="UTF-8")
# line = f.readline()
# print(line)
# f.close()

# f=open("새파일.txt",'r')
# while True:
#     line = f.readline() # 한줄씩 불러옴
#     if not line: break
#     print(line)
# f.close()

#readlines()
# f=open("새파일.txt",'r')
# lines = f.readlines() # 파일에 있는 모든 라인을 불러온다. 리스트형식
# for line in lines:
#     print(line)
# f.close()

#readline()
# f=open("새파일.txt",'r')
# data = f.read() #통째로 불러옴.
# print(data)
# f.close()

# 'w'== write는 지우고 새로운 글써짐. 'a'== 이어서 글 작성.
# f=open("새파일.txt",'a',encoding="UTF-8")
# for i in range(11,20):
#     data = "%d번째 줄 입니다. \n" %i
#     f.write(data)
# f.close()

# with문 사용하기  == close 필요x
# with open('foo.txt','w') as f:  # f에 저장 (지역변수)
#     f.write("life")


