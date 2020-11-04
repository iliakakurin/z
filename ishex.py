h = '0123456789abcdefABCDEF'
s = input()
corr = True
if s[0] == '0':
    corr = False
for x in s:
    if x not in h:
        print('NO')
        corr = False
if corr == True:
    print('YES')
