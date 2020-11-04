n = int(input())
a = input()
b = input()
corr = True
for x in a:
    if int(x) >= n:
        corr = False
for x in b:
    if int(x) >= n:
        corr = False
if corr:
    c = int(a, base=n)
    d = int(b, base=n)
    e = c + d
    res = ''
    while e > 0:
        res = str(e % n) + res
        e = e // n
    print(res)
else:
    print('Wrong input!')

