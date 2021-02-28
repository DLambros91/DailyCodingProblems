import sys

stack = []

arr = ['15', '7', '1', '1', '+', '-', '/', '3', '*', '2', '1', '1', '+', '+', '-']

val = sys.maxsize

def applyOp(a, b, c):
    if b is '+':
        return a + c
    elif b is '-':
        return a - c
    elif b is '/':
        return a / c
    else:
        return a * c

for i in arr:
    if str.isdigit(i):
        stack.append(int(i))
    else:
        if val is sys.maxsize:
            t2 = stack.pop()
            t1 = stack.pop()
            val = applyOp(t1, i, t2)
            print('New val', val)
        else:
            val = applyOp(stack.pop(), i, val)
            print('New val', val)

print('Final val', val)
assertTrue(val, 5)
