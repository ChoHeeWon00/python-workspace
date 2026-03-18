class MyClass:
    def test(self): #self this 와 같은 의미
        print("test 메소드")
        print(self)

c = MyClass()
c.test()
print( c )

class MyClass02:
    def sumFunc(self, n1, n2):
        return n1 + n2
    def printFunc(self, n1, n2, sum_ ):
        print(f"{n1} + {n2} = {sum_}")
    def inputFunc(self):
        n1 = int( input("1 수 입력 : ") )
        n2 = int( input("2 수 입력 : ") )
        return n1, n2;          
my = MyClass02()
num1, num2 = my.inputFunc();
result = my.sumFunc(num1, num2);
my.printFunc(num1, num2, result)
