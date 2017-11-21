#class A
class A:
    text = ''
    def __init__(self, test):
        self.text = test
    def test(self):
        print(self.text)

#class B
class B:
    def __init__(self):
        pass
    
    def printStar(self):
        for i in range(1, 73):
            print("*", end = "")
        print()
        
    def NineProductNine(self):
        for i in range(1, 10):
            for j in range(1, 10):
                print('%d*%d=%2d' % (j, i, i * j), end ='  ')
            print()

#Container
class Container:
    _classname = None
    def __init__(self, classname):
        self._classname = classname
    def execute(self):
        return self._classname

def main():
    container = Container(B()).execute()
    container.printStar()
    container.NineProductNine()
    container.printStar()

    container2 = Container(A("你好")).execute()
    container2.test()
main()

