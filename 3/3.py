def d(l):
    x = int(dict[(dict.find(l)+4)])
    if(dict[(dict.find(l)+5)] == "/"):
        if(dict[(dict.find(l)+5)] == "1"):
            return x/((int(dict[(dict.find(l)+6)]))*10)
        return x/int(dict[(dict.find(l)+6)])
    return x
def d2(l):
    x = int(dict[(dict.find(l)+2)])
    if(len(dict)-1 > (dict.find(l)+3)):
        if(dict[(dict.find(l)+3)] == "/"):
            if(dict[(dict.find(l)+3)] == "1"):
                return x/((int(dict[(dict.find(l)+4)]))*10)
            return x/int(dict[(dict.find(l)+4)])
    return x

    return x
'''
    num1 = int(dict[(dict.find(letra)+4)])

    if(dict[(dict.find(letra)+5)] == '/'):
        num2 = int(dict[(dict.find(letra)+6)])
        if(dict[(dict.find(letra)+7)] == "0"):
            num2 = (num2*10) + int(dict[(dict.find(letra)+7)])
        return num1/num2
    else:
        return num1

def d2(letra):
    num1 = int(dict[(dict.find(letra)+2)])

    if(dict[(dict.find(letra)+2)] == '/'):
        num2 = int(dict[(dict.find(letra)+3)])
        if(dict[(dict.find(letra)+5)] == "0"):
            num2 = (num2*10) + int(dict[(dict.find(letra)+4)])
        return(num1/num2)
    else:
        return num1
'''
a = []
i = 1
b = int(input())
while(b!=0):
    a.append(input())
    b -= 1
j = 0
p1 = ""
p2 = ""
vp1 = 0
vp2 = 0
c = []
datos = ""
c = list(a[0])
a.append("%")
contar = 1
while(a[0] != "%"):
    j = 0
    p1 = ""
    p2 = ""
    vp1 = 0
    vp2 = 0
    c = list(a[0])
    num1 = 0
    num2 = 0
    while(c[0][0] != "-"):
        p1 = p1 + c[0]
        c.pop(0)
    c.pop(0)
    while(c[0][0] != '|'):
        p2 = p2 + c[0]
        c.pop(0)
    c.pop(0)
    datos = c
    dict = "".join(datos)
    if(datos[0] == "{" or datos[0] == "["):
        while(len(p1) != j):
            vp1 += d(p1[j])
            j += 1
        j = 0
        while(len(p2) != j):
            vp2 += d(p2[j])
            j += 1
    else:
        while(len(p1) != j):
            vp1 += d2(p1[j])
            j += 1
        j = 0
        while(len(p2) != j):
            vp2 += d2(p2[j])
            j += 1   
    resultado = p1 if vp1 > vp2 else (p2 if vp1 < vp2 else "-")
    print("Case #", contar, ": ", resultado, sep="")
    contar += 1

    a.pop(0)
    j = 0


#PROBLEMA CON LOS DIVISORES
#Prubea DropBox
'''
10
love-hate|a=2,e=4,h=3,l=5,o=1,t=6,v=0
low-high|[('g', 1/3), ('h', 2), ('i', 1/9), ('l', 4), ('o', 0), ('w', 1/8)]
clever-stupid|c=6/9,d=5/6,e=8/9,i=1/7,l=0,p=8/10,r=5/10,s=6/9,t=5/6,u=4/10,v=3/8
lose-find|{'d': 3, 'e': 0, 'f': 5, 'i': 2, 'l': 1, 'n': 4, 'o': 7, 's': 6}
win-lose|e=1,i=4,l=2,n=0,o=6,s=3,w=5
blame-praise|[('a', 5), ('b', 8), ('e', 4), ('i', 2), ('l', 0), ('m', 1), ('p', 3), ('r', 6), ('s', 7)]
false-true|{'a': 7/9, 'e': 2/5, 'f': 3, 'l': 0, 'r': 7, 's': 2, 't': 5, 'u': 1/5}
soft-hard|a=0,d=1,f=4,h=7,o=2,r=5,s=6,t=3
rough-smooth|g=7/10,h=7/9,m=3,o=4,r=6,s=1,t=4/5,u=3/10
tame-wild|{'a': 1, 'd': 5, 'e': 3, 'i': 0, 'l': 2, 'm': 4, 't': 7, 'w': 6}
1
love-hate|a=2,e=4,h=3,l=5,o=1,t=6,v=0


'''