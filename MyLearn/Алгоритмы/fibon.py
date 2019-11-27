

def fibon(nuber):
    if nuber == 1:
        return 0
    elif nuber == 2:
        return 1
    return fibon(nuber-1)+fibon(nuber-2)

print(fibon(121))