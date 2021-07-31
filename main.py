class TheExample:
    def __init__(self):
        self.f4()

    def f(self):
        return self.a + self.b

    def f1(self):
        return self.a - self.b

    def f2(self):
        return self.a * self.b

    def f3(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b

    def f4(self):
        self.a = int(input())
        self.b = int(input())

while True:
    print("+, -, *, /")
    x = input()
    print("Введите 2 числа:")
    ex = TheExample()
    if x == int:
        break
    if x == "+":
        print(ex.f())
    if x == "-":
        print(ex.f1())
    if x == "*":
        print(ex.f2())
    if x == "/":
        print(ex.f3())
