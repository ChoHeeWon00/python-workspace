class MyClass:
    def test(self):
        print("myclass 기능")
class TestClass(MyClass):
    def testClass(self):
        print("testclass 기능")

tc = TestClass()
tc.test()
tc.testClass()

class AAA:
    def aaa(self):
        print("aaa 기능")
class BBB:
    def bbb(self):
        print("bbb 기능")
    def test(self):
        print("bbb test")
class CCC(AAA, BBB):
    def ccc(self):
        print("ccc 기능")
        super().test() #self.test()
    def test(self):
        print("자식 test")
c = CCC()
c.aaa()
c.bbb()
c.ccc()