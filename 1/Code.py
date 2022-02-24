a = []
i = 1
b = int(input())
while(b!=0):
    a.append(input())
    b -= 1


for j in a:
    c = int(a[i-1][0]) + int((a[i-1][2])) + 1
    if(c == 13):
        c = "-"
    print("Case #", i, ": ", c, sep="")

    i += 1