f = open('24.txt')
s = f.readline()
flag1 = False
flag2 = False
k1 = 0
k2 = 0
maxk = 0
start1 = False
for i in range(len(s)):
    if s[i] == 'Z' and flag1 == False:
        flag1 = True
        k1 += 1
        start1 = True
        maxk = max(k1, maxk)
    elif s[i] == 'Z' and flag1 == True:
        k1 = 0
        flag1 = False
    else:
        k1 += 1
        maxk = max(k1, maxk)

    if start1 == True:
        start1 = False
        k2 = 0
        flag2 = False
        continue

    if s[i] == 'Z' and flag2 == False:
        k2 += 1
        maxk = max(k2, maxk)
        flag2 = True
    elif s[i] == 'Z' and flag2 == True:
        k2 = 0
        flag2 = False
    else:
        k2 += 1
        maxk = max(k2, maxk)
print(maxk)
f.close







































f.close


