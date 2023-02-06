def main():
    x = int(input("what is x: "))
    y = int(input("what is y: "))
    added(x, y)
    sub(x, y)
    module(x, y)
    multiplication(x, y)
    div(x, y)


def added(x, y):
    print(x)
    print(y)
    print(x+y)


def sub(x, y):
    print(x)
    print(y)
    print(x-y)


def module(x, y):
    print(x)
    print(y)
    print(x%y)


def multiplication(x, y):
    print(x)
    print(y)
    print(x*y)


def div(x, y):
    print(x)
    print(y)
    print(x/y)


main()
