h = '0123456789abcdef'
s = input()
corr = True
for x in s:
    if x not in h:
        print('NO')
        corr = False
if corr == True:
    print('YES')
