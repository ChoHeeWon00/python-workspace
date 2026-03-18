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

num = 1234
def test():
    global num
    num = "다른변경"
    abcd="test";
    print( num )
test();
print("num 출력 : ", num)

#print( abcd )