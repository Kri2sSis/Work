

a = [1,2,[3,4,[5,6,[7,8,[9]]]]]

def rec(mass,level=1):
    print(*mass,' level ', level)
    for i in mass:
        if type(i) == list:
            rec(i,level+1)


rec(a)