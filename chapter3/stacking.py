def a():
    print("a()return")
    b()
    d()
    print("a()return")

def b():
    print("b() return")
    c()
    d()
    print("b() return")

def c():
    print("c() return")
    print("c() after")

def d():
    print("d() return")
    print("d() after")

a()