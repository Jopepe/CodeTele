n = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
def control(i):
    if(11< i):
        i = i - len(n)
        return(i)
    else:
        return(i)
#print(n[control(i)])
a = []
j = 1
b = int(input())
while(b!=0):
    h = []
    h.append(input())
    p = input() + "!"
    h.append(p) 
    a.append(h)
    b -= 1
a.append("|")
print("\n"*40)
while(a[0] != "|"):
    letraini = a[0][0]
    a[0].pop(0)
    posi = str(letraini)
    i = n.index(letraini)
    tex = letraini
    tempo = list(a[0][0])
    while(tempo[0] != "!"):
        if(tempo[0] == "T"):
            i +=2
        else:
            i +=1
        tex = tex + n[control(i)]
        tempo.pop(0)
    print("Puebras: ", tex)
    tex = ""
    a.pop(0)

'''
3
G
TTTsTTs
A
sTTsTTT
A
TTsTTsT
'''
