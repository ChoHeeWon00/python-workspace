class AAA:
    def aaa(self):
        print("aaa 기능")
class BBB(AAA):
    def bbb(self):
        print("bbb 기능")
    def aaa(self):
        print("bbb의 aaa 기능")
b = BBB()
b.aaa()
b.bbb()


class CCC:
    name : str
    def __init__(self):
        self.test = "test 값"
        self.name = "이름이 들어값"
    def ccc(self, num : int) -> int:
        print(num)
        return 100;
c = CCC()
c.ccc(100)
print( c.test )
print( c.name )
