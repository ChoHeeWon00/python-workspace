class TestClass:
    #n1 = 100
    def test01(self):
        self.n1 = 100
        print("test01 : ", self.n1 )
    def test02(self):
        print("test02 : ", self.n1 )
    def test03(self):
        print("test03 : ", self.n2)

tc = TestClass()
tc.test01()
tc.test02()
tc.n2 = 12345;
tc.test03()

class TestClass02:
    def __init__(self, name="김개똥", age=30, addr=None):
        self.name = name;
        self.age = age
        self.addr = addr
    def test01(self):
        print(self.name)
        print(self.age)
        print(self.addr)
    #def test01(self, *par ):
    #    print("실행??? : ", par)
    def __str__(self):
        #return "객체 정보???"
        return f"{self.name}, {self.age}, {self.addr}"
    
tc = TestClass02("홍길동")
tc.test01()
#tc.test01(10,20,30)
tc = TestClass02()
tc.test01()
print( tc )