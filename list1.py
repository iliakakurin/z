k = int(input())
count = 0
for i in range(1, k + 1):
    s = str(i)
    x = s[::-1]
    if s == x:
        count += 1
print(count)
