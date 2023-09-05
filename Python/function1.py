# defining function

def add (arg1, arg2):
    total = arg1 + arg2
    return total
out = add(1,5)
print(out)

def adder (arg1, arg2):
    total = arg1 + arg2
    print(total)
adder(10,20)

def sum (arg):
    x = 0
    for i in arg:
        x = x + i
    return x
out = sum([10,20,40])
print(out)