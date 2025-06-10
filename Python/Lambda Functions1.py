'''
def calculate (a,b):
    return a*a+2*a*b+b*b
print(calculate(2,3))
'''
print((lambda a,b :a*a+2*a*b+b*b)(2,3))

a = (lambda a,b :a*a+2*a*b+b*b)(2,3)
print(a)

b = (lambda x: x*x*x)(4)
print(b)