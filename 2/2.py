a = []
i = 0
h = []
b = int(input())
while(b!=0):
    f = input()
    
    i = int(f[0])
    a.append(i)
    while(i != 0):
        a.append(input())
        i -= 1
    
    e = int(f[2])
    while(e != 0):
        a.append(input())
        e -= 1
    i = int(f[0])
    a.append("|")
    h.append(a)
    a = []
    f = []
    b -= 1
print("\n")
print(h)
print("\n")
while(len(h) != 0):
    print(h[0])
    while(h[0][0] != "|"):
        print(h[0][0])
        h[0].pop(0)

    h.pop(0)
    print("\n")
'''
j = 0
palabras = []
de = []
#print(h[0])
while(len(h) != 0):
    l = len(h[0])
    while(l != 1):
        numero = int(h[0][0])
        h[0].pop(0)
        while(numero != 0):
            palabras.append(h[0][0])
            h[0].pop(0)
            numero -= 1
        numero = len(h[0])
        while(numero != 0):
            de.append(h[0][0])
            h[0].pop(0)
            numero -= 1
        final = "".join(de)
        print("Case #", j+1, ":", final, sep="")
        l = len(h[0])
    h.pop(0)
    print(h)
    j += 1
    palabras = []
    de = []


uu




2
1 4 6
SNORLAX
T A K E C A
S N O R L A
X R E W I T
H V E N O M
2 3 10
PIKACHU
CHARIZARD
N O P O K E M U H C
A K I C H A R I Z A
R D P O N S H E R E
'''