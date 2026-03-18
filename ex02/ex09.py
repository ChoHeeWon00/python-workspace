class TestClass:
    name = "홍길동"
    def __init__(self):
        self.addr = "주소저장"
    @classmethod
    def test01(cls):
        print("test01 ", cls.name )
#tc = TestClass()
TestClass.test01()
print( TestClass.name )
#print( TestClass.addr )