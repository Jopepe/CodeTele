a = []
i = 0
h = []
b = int(input())
while(b!=0):
    f = input()
    f = list(f)
    i = int(f[0])
    if(f[1] != " "):
        i = (i*10) + int(f[1])
        if(f[2] != " "):
            i = (i*10) + int(f[2])
            f.pop(2)
        f.pop(1)  
    f[0] = i    
    a.append(i)
    while(i != 0):
        a.append(input())
        i -= 1
    
    e = int(f[2])
    if(f[3] != " "):
        e = (e*10) + int(f[3])
        if(f[4] != " "):
            e = (e*10) + int(f[4])    
    while(e != 0):
        a.append(input())
        e -= 1
    i = int(f[0])
    a.append("|")
    h.append(a)
    a = []
    f = []
    b -= 1
palabras = []
textof = [] 
texto = ""
numplabra = 1
caso = 1
while(len(h) != 0):
    numplabra = int(h[0][0])
    numplabra2 = numplabra
    while(h[0][0] != "|"):
        h[0].pop(0)
        if(numplabra != 0):
            palabras.append(h[0][0])
            numplabra -= 1
        textof.append(h[0][0])
    while(numplabra2 != 0):
        textof.pop(0)
        numplabra2 -= 1
    textof.pop(len(textof)-1)
        
    contar = len(palabras)
    texto = "".join(textof)
    texto = texto.replace(' ', '')
    k = 0
    control = True
    lenpa = len(palabras)
    while(lenpa != 0):

        pala = palabras[k]
        palarev = pala[::-1]
        if(pala in texto):
            texto = texto.replace(pala, '')
            palabras.pop(k)
            k = 0
        elif(palarev in texto):
            texto = texto.replace(palarev, '')
            palabras.pop(k)
            k = 0
        else:
            k += 1
        lenpa = len(palabras)
        
    
    #Case #2: NOPOKEMONSHERE
    print("Case #", caso,": ", texto, sep="")
    caso += 1

    h.pop(0)
    palabras = []
    texto = ""
    textof = []
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


uus




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