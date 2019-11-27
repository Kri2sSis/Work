

def palidrom(s):
    if len(s) <= 1:
        return True
    if s[0]!=s[-1]:
        return False
    return palidrom(s[1:-1])

print(palidrom("aa"))