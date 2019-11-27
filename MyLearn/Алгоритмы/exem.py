

def num(number):
    if number % 100 < 10:
        return number
    else:
        check = number % 10
        return check + num(number//10)

a = num(99)
if a >10:
    print(num(a))
else:
    print(a)













