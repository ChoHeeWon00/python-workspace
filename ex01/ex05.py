'''
num = 2;
if (num == 1):
  print(111)
  print("일일일")
else:
  print("else 실행")
print("다음문장")
'''
'''
num = 10;
if num > 0:
    print("양의 : " , end=" ")
    if num % 2 == 0:
        print("짝")
    else:
        print("홀")
else:
    print("음수")
'''
'''
num = 50;
if num > 100:
    print("100보다 크다")
elif num > 50:
    print("50보다 크다")
else:
    print("그 외의 값")
'''
name = None
while True:
    print("=="*20)
    print("1.이름 입력"); print("2.성적 3과목 입력")
    print("3.이름출력"); print("4.합")
    print("5.평균"); print("6.종료"); print("=="*20)
    num = int( input(">>> : ") )
    if num == 1: name = input("이름 입력 : ")
    elif num == 2:
        kor = int(input("국어 입력 : "))
        eng = int(input("영어 입력 : "))
        math = int(input("수학 입력 : "))
    elif num == 3:
        print("이름 출력 : ",name)
    elif num == 4:
        avg = (kor+eng+math) / 3
        print("합 : ", (kor+eng+math))
    elif num == 5:
        print("평균 : ",avg)
    elif num == 6:
        break;