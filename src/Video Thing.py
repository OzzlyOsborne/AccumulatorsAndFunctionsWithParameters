def main():
    print("main")
    n = 1
    a = foo(n)
    b = bar(n)
    print(a, b)


def foo(n):
    n = n * 2
    print(n)


def bar(x):
    x = x + 2
    return x
    print("return")

main()