import sys

a = 10

def f():
    global a
    a = max(a, 20)
    print(a)


if __name__ == "__main__":
    f()
    print(a)