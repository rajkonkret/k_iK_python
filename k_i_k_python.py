
# tic tac toe
import os
import random
from tkinter import Tk, LabelFrame, Button, OptionMenu, StringVar
tablica = [" "," "," "] *3
tablicaarg= [0,0,0] *3
#tablshadow=[" "," "," "] *3
szablwygr =(-2,-1,1,2)
index=[0]
q=1
c1=''
gracz="X"
def czypuste():
    puste=0
    for i in range(0,9):
        if tablica[i] == ' ':
            puste=1
    return puste
def ruchkomp(tbl):
    maks=0
    index=[]
    tablshadow=[]
    for x in range(0,9):
        if tablicaarg[x]!=99:
            maks1=tablicaarg[x]
            if maks1>maks:
                maks=maks1
    co=tablicaarg.count(maks)
    for t in range(0,9):
        if tablicaarg[t]==maks:
            inx=tablicaarg.index(maks)
            index.append(t)

    print('maks={},ile={},{}'.format(maks,co,index))
   # cox=random.randint(0,co)
    rk=random.randint(0,len(index)-1)
    print('index={}'.format(index) )
    #while index[rk]==0:
     #    rk=random.randint(0,8)
    #print(rk)
    #rkx=int(rk/3)
    #print (rkx)
    #rky=rk -rkx*3
    #print (rky)
    #rk=tablicaarg.index(maks)
    print('rk={},index[r]={}'.format(rk,index[rk-1]))
    rk=index[rk-1]
    #tablshadow=tbl.copy()
    for t in range (0,len(index)):
        tablshadow=tbl.copy()
        print('tbl 1:{}'.format(tbl))
        print('tbl sh:{}'.format(tablshadow))
        xsh=index[t]
        print('xsh {}'.format(xsh))
        tbl[xsh]='X'
        print('tbl 2:{}'.format(tbl))
        kon=czykon()
        if kon=='X' :
            rk=index[t]
        tbl[xsh] =' '
        tbl = tablshadow.copy()
        print('tbl 3:{}'.format(tbl))
    tbl = tablshadow.copy()
    tablica=[]
    tablica = tablshadow.copy()
    print('tbl 4:{}'.format(tablica))
    print ('tablica po operacjach')
    ryspla()
    #for t in range(0,8):
     #   index[t]=0
    return rk
def czykon():
    graczwygrany=''
    if (tablica[0*3+(1-1)]=='X' and tablica[(0)*3+(2-1)]=='X' and tablica[(1-1)*3+(3-1)]=='X'):
	    graczwygrany='X'

    if (tablica[1*3+(1-1)]=='X' and tablica[(1)*3+(2-1)]=='X' and tablica[(1)*3+(3-1)]=='X'):
	    graczwygrany='X'
    if (tablica[2*3+(1-1)]=='X' and tablica[(2)*3+(2-1)]=='X' and tablica[(2)*3+(3-1)]=='X'):
	    graczwygrany='X'

    if (tablica[0*3+(1-1)]=='O' and tablica[(0)*3+(2-1)]=='O' and tablica[(1-1)*3+(3-1)]=='O'):
	    graczwygrany='O'

    if (tablica[1*3+(1-1)]=='O' and tablica[(1)*3+(2-1)]=='O' and tablica[(1)*3+(3-1)]=='O'):
	    graczwygrany='O'

    if (tablica[2*3+(1-1)]=='O' and tablica[(2)*3+(2-1)]=='O' and tablica[(2)*3+(3-1)]=='O'):
	    graczwygrany='O'
    if (tablica[0*3+(1-1)]=='O' and tablica[(1)*3+(1-1)]=='O' and tablica[(2)*3+(1-1)]=='O'):
	    graczwygrany='O'
    if (tablica[0*3+(1)]=='O' and tablica[(1)*3+(1)]=='O' and tablica[(2)*3+(1)]=='O'):
	    graczwygrany='O'
    if (tablica[0*3+(2)]=='O' and tablica[(1)*3+(2)]=='O' and tablica[(2)*3+(2)]=='O'):
	    graczwygrany='O'
    if (tablica[0*3+(1-1)]=='X' and tablica[(1)*3+(1-1)]=='X' and tablica[(2)*3+(1-1)]=='X'):
	    graczwygrany='X'
    if (tablica[0*3+(1)]=='X' and tablica[(1)*3+(1)]=='X' and tablica[(2)*3+(2)]=='X'):
	    graczwygrany='X'
    if (tablica[0*3+(2)]=='X' and tablica[(1)*3+(2)]=='X' and tablica[(2)*3+(2)]=='X'):
	    graczwygrany='X'
    if (tablica[0*3+(0)]=='X' and tablica[(1)*3+(1)]=='X' and tablica[(2)*3+(2)]=='X'):
	    graczwygrany='X'
    if (tablica[2*3+(0)]=='X' and tablica[(1)*3+(1)]=='X' and tablica[(0)*3+(2)]=='X'):
	    graczwygrany='X'
    if (tablica[0*3+(0)]=='O' and tablica[(1)*3+(1)]=='O' and tablica[(2)*3+(2)]=='O'):
	    graczwygrany='O'
    if (tablica[2*3+(0)]=='O' and tablica[(1)*3+(1)]=='O' and tablica[(0)*3+(2)]=='O'):
	    graczwygrany='O'

    return graczwygrany;

def ryspla():
    os.system("cls")
    print ("|{}|{}|{}|".format(tablica[0],tablica[1],tablica[2]))
    print("|-+-+-|")
    print ("|{}|{}|{}|".format(tablica[3],tablica[4],tablica[5]))
    print("|-+-+-|")
    print ("|{}|{}|{}|".format(tablica[6],tablica[7],tablica[8]))
    #print ('Hello World')
def wstawgracza(gracz,a,b):
#   print (gracz)
    plus=1
    if gracz=='O' :
        plus=2
    tablica[(a-1)*3+(b-1)]=gracz
    tablicaarg[(a-1)*3+(b-1)]=99
    print (a,b)
    for tx in szablwygr:
        txtest=0
        z=(a)+tx

        if z in range(1,4):
            txtest = tablicaarg[((z)-1)*3+(b-1)]
            if txtest!=99:
                txtest=txtest+plus
                tablicaarg[((z)-1)*3+(b-1)]=txtest
        z=(b)+tx

        if z in range(1,4):
            txtest = tablicaarg[((a)-1)*3+(z-1)]
            if txtest!=99:
                txtest=txtest+plus
                tablicaarg[((a)-1)*3+(z-1)]=txtest
        z1=(b)+tx
        z2=a+tx

        if z1 in range(1,4) and z2 in range(1,4) and (z1+z2)%2==0:
            txtest = tablicaarg[((z2)-1)*3+(z1-1)]
            if txtest!=99:
                txtest=txtest+plus
                tablicaarg[((z2)-1)*3+(z1-1)]=txtest
        z1=(b)-tx
        z2=a+tx

        if z1 in range(1,4) and z2 in range(1,4) and (z1+z2)%2==0:
            txtest = tablicaarg[((z2)-1)*3+(z1-1)]
            if txtest!=99:
                txtest=txtest+plus
                tablicaarg[((z2)-1)*3+(z1-1)]=txtest
        print(z,a,b,tx,txtest)
    print('tablicaarg')
    print ("|{}|{}|{}|".format(tablicaarg[0],tablicaarg[1],tablicaarg[2]))
    print("|-+-+-|")
    print ("|{}|{}|{}|".format(tablicaarg[3],tablicaarg[4],tablicaarg[5]))
    print("|-+-+-|")
    print ("|{}|{}|{}|".format(tablicaarg[6],tablicaarg[7],tablicaarg[8]))
    #print ('Hello World')
#a = input("wiersz")
#b = input("?")
#print (a)
#print(b)
#print (a+b)
#a=int(a)
#b=int(b)
#print (a+b)
#tablica[a,b]=1
#tablica.append(99)
odpo=input('start gry (t/n)')

if odpo != 'n':
    q=0
while q==0:
    if gracz == "X":
        gracz="O"
    else:  gracz="X"
#   wstawgracza("x")
#	os.system("cls")
	#print ('\033[2J\033[0;0H')
	#for z in tablica:
#	print ("|{}|{}|{}|".format(tablica[0],tablica[1],tablica[2]))
#	print("|-+-+-|")
#	print ("|{}|{}|{}|".format(tablica[3],tablica[4],tablica[5]))
#	print("|-+-+-|")
#	print ("|{}|{}|{}|".format(tablica[6],tablica[7],tablica[8]))
 	#  print ((a-1)*3+(b-1))
	#print (tablica[(a-1)*3+(b-1)])
	#print("{}+{} ={} ".format(a,b,a+b))
	#print ('\033[2J\033[0;0H')

    ryspla()
    c2=czypuste()
    c1=czykon()
    if c2==0 and c1=='':
        print('Remis')
        break
#    c1=czykon()
    print('{}'.format(c1))
    if c1!='' :
        print ('wygrał {}'.format(c1))
        break
 #   odpo=input('start gry (t/n)')

  #  if odpo != 't':
#	    q=1
    print ("ruch gracza: {}".format(gracz))
    if gracz != 'X':
        a = input("wiersz: ")
        b = input("kolumna: ")
        a=int(a)
        b=int(b)
#   tablica[(a-1)*3+(b-1)]="X"
    else:
        rka=ruchkomp(tablica)
        print("rka=",rka)
        a=int(rka/3)
        print ("a=",a)
        b=int(rka - a*3)
        print('b=',b)
        a=a+1
        b=b+1
        print ('a={},b={}'.format(a,b))
    if tablica[(a-1)*3+(b-1)]==" ":
        wstawgracza(gracz,a,b)
    else: print ("błąd")
    c1=czykon()
    if c1=='X' :
        print ('wygrał X')

#   os.system("cls")
#   print ("|{}|{}|{}|".format(tablica[0],tablica[1],tablica[2]))
#  print("|-+-+-|")
#  print ("|{}|{}|{}|".format(tablica[3],tablica[4],tablica[5]))
#  print("|-+-+-|")
#  print ("|{}|{}|{}|".format(tablica[6],tablica[7],tablica[8]))
 #   input("pause")
    ryspla()
#    gui = Tk()
#    gui.resizable(0, 0)
#    gui.title("")
#    fra1 = LabelFrame(gui, text="Stary zestaw znaków")
#   input("pause")
'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Koniec meczu')
input("pause")
#import re

#str = "The rain in Spain"
#x = re.search("rj", str)
#rj =input ()
#rj1=re.search("\d",rj)
#if rj1 != None :
#    print(rj1.string) #this will print an object
#else:

#    print ("to nie cyfra")








