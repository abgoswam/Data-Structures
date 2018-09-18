c = 1  # global variable


def add():
    global c
    c = c + 2  # increment c by 2
    print(c)


add()
print(c)