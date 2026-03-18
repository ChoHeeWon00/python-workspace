'''
sum_ = 0
num = 10
for i in range( num+1 ): #(0, 11, 1)
    sum_ += i
print( sum_ )
'''
'''
def sumFunc():
    sum_ = 0
    num = 10
    for i in range( num+1 ): #(0, 11, 1)
        sum_ += i
    print( sum_ )
sumFunc();
'''
'''
def sumFunc( num : int  ):
    sum_ = 0
    #num = 10
    for i in range( num+1 ): #(0, 11, 1)
        sum_ += i
    print( sum_ )
sumFunc( 20 );
'''
'''
def sumFunc( num ) -> int:
    sum_ = 0
    for i in range( num+1 ): #(0, 11, 1)
        sum_ += i
    #print( sum_ )
    return sum_
sum2 = sumFunc( 10 );
print( sum2 )
'''
'''
num = 1234
def test():
    global num
    num = "다른변경"
    abcd="test";
    print( num )
test();
print("num 출력 : ", num)

#print( abcd )

'''
'''
def test(n1, n2, n3=1234):
    print(n1, n2, n3)
test(10,20)
test(10,20,30)
'''
def test(*par): 
    print( type(par), par )
test(1,2,3,4)

def test2(name:"none", aaa:None, age:10):
    print(name, aaa, age)
test2( aaa=10 , age=20 , name="홍길동" )
test2(1,2,3)

def test3( **par ):
    print( par )
test3( aaa=10 , age=20 , name="홍길동" )

def test4(num : int) -> int:
    return num + 100
result = test4(100)
print( result )

resultLam = lambda a : a+1000
print( resultLam(1000) )


def test5(a, b):
    #if a>b: 
    # return a
    #else: 
    # return b
    return a if a > b else b
print( test5(100,20) )

big = lambda a,b : a if a > b else b
print( big(1000,200) )

def test6(num : int) -> str:
    print("test6 : ", num)
    return str(num)
re = test6(100)

strLam = lambda n : str(n)
print( type( strLam(100) ) )

li = [10,20,30]
reLi = list( map(test6 , li ) )
print( type(reLi) )
print( reLi )
print( list( map(int , reLi ) ) )
