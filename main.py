import random
#zad1
A = [x for x in range(1,11)]
B = [4**x for x in range(0,8)]
C = [x for x in B if x%2==0]
#print(B)

#zad2
random.seed()
lista1 = [random.randint(0,10) for x in range(10)]
lista2 = [x for x in lista1 if x%2==0]
#print(lista2)

#zad3
listaProduktow = {"Chleb":"szt","Pomidor":"kg","Ziemniaki":"kg","Jogurt":"szt","Mleko":"l"}
listaProdSzt = {key: value for key,value in listaProduktow.items() if value=="szt"}
#print(listaProdSzt)

#zad4
def SprCzyTrojkatProstokatky(katPierwszy, katDrugi):
    if(katPierwszy+katDrugi==90):
        return True
    else:
        return False

#zad5
def PoleTrapezu(a=2,b=4,h=3):
    return ((a+b)*h)/2

#zad6
def IloczynCiagu(a1=1,b=4,ile=10):
    aile=a1*(ile-1)*b
    return ((a1+aile)/2)*ile
#print(IloczynCiagu())

#zad7
def IloczynCiagu(* args):
    if len(args)<3: return 0
    aile=args[0]*(args[2]-1)*args[1]
    return ((args[0] + aile) / 2) * args[2]

#print(IloczynCiagu(1,4,10))

#zad8

def ListaZakupow( **lista):
    ilosc=len(lista)
    suma=0
    for p in lista:
      suma += lista[p]
    return suma
#print(ListaZakupow(chleb=7,makaron=2.5))

#zad9
import Ciagi

#zad10
f = open("liczby.txt","w")
for x in range(0,100):
    if(x%4==0):
        f.write(str(x))
        f.write(" ")

#zad11
f=open("liczby.txt","r")
print(f.read())

