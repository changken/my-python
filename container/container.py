#class A
class A:
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
    def __init__(self):
        self._classnameList = {}

    def add(self, className , classInstance):
        self._classnameList[className] = classInstance

    def get(self, className):
        return self._classnameList[className]

if __name__ == "__main__":
    def main():
        container = Container()
        #addition class name and its instance
        container.add("A", A("你好喔！"))
        container.add("B", B())

        #use it!
        b = container.get("B")
        b.printStar()
        b.NineProductNine()
        b.printStar()

        a = container.get("A")
        a.test()
    main()

