def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello!")
        fx(*args, **kwargs)
        print("thanks for using this function")
        print("\n")
    return mfx
@greet
def add(a,b):
    print(a+b)

@greet
def hello():
    print("hello world")
@greet
def mult(a,b):
    print(a*b)

hello()
add(4,5)
mult(4,5)

