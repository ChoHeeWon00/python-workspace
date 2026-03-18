for i in range(1, 5, 1): #(i=1, i<5 , i++)
    print(i)
print("="*20)
for i in range(1, 5, 1): #(i=1, i<5 , i++)
    if i % 2 == 0:
        print(i)

print("="*20)
str ="test str"
for i in str:
    print(i)

print("="*20)
list = [1,2,"안녕",1.123]
for i in list:
    print(i)

print("="*20)
print( "안녕1" in list )
result = None
if "안녕" in list:
    result = "존재한다";
else:
    result ="없다"
print("결과 : ",result)

result = "참인경우" if "안녕" in list else "거짓인경우";
print("결과 : ",result)
print("="*20)
list = [1,2,3,4,5]
number = [x for x in list]
print( number )

number = [x for x in list if x % 2 == 0 ]
print( number )

