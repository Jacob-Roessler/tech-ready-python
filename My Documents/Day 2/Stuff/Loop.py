x = 0
size = int(input("Enter a number to count up to: "))
def loop(size,x = 0):
    print(x)
    x+=1
    if x > size:
        return 0
    loop(size, x)
loop(size, x)