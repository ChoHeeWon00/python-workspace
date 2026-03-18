n1 = 10
n2 = 2
try:
    result = n1 / n2
    #print("결과 : ", result)
    print( n1 + "문자열" )
except ZeroDivisionError:
    print("예외 상황")
except:
    print("연산 불가")
else:
    print("예외 없는 경우 마지막에 실행")
    print("결과 : ", result)
finally:
    print("무조건 실행되는 코드")

print("다음 문장")

print("파일 입출력")
file = None
try:
    file = open("C:\\ibm3-workspace/python-workspace/test.txt","r")
except FileNotFoundError:
    print("파일이 없습니다")
else:
    print("else : ", file)
    print( file.read() )
finally:
    if file != None:
        file.close();
    print("file : ", file)

try:
    age = int( input("나이 입력 : ") )
    if age < 1:
        #raise
        raise Exception("잘못 입력")
except ValueError:
    print("숫자를 입력하세요")
except Exception as e:
    print("exception : ", e)
except:
    print("0살 이하의 나이 없음")
else:
    print("당신 나이 : ", age)
finally:
    print("프로그램 종료")