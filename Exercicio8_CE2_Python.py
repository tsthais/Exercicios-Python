#!/usr/bin/env python
# coding: utf-8

# **Lista de exercícios 8**
# 
# Thaís da Silva Santos 
# 
# 
# 16/045821
# 

# In[1]:


import random

def escolhe(matricula):
    random.seed(matricula)
    cap1 = (2,8,9,11,12,15,16,18,20,21,22,24,26,27,28,30,31,32)    
    cap2 = (36,40,44,45,46,48,50,51,53,55,56,57,59,60)
    cap3 = (63,64,65,68,71,72,74,76,78,80,81,84)
    cap4 = (85,86,87,89,91,92,94,97,99,101,103,104,106)
    cap5 = (111,115,117,118,119,122,123,124,126,127,131,132,133)
    cap6 = (138,139,140,141,144,147,148)
    cap7 = (152,153,154,155,157,160,161,164,165,166,168,171,172)
    cap8 = (174,175,176,177,179,181,182,185)
    return(random.sample(cap8, k=2))

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula")))


# Exercício 182

# In[1]:


palavra = input("Escreva uma palavra: ")


# In[2]:


elementos = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Uut Fl Uup Lv Uus Uuo".split()

def encontrar(palavra):
    proximo = [False for x in range(len(palavra)+1)]
    proximo[0] = []

    for i in range(1, len(palavra)+1):
        possiveis = list()
        for j in range(max(i-3,0), i):
            if proximo[j] == False:
                continue
            elemento = palavra[j:i].title()
            if elemento in elementos:
                possiveis.append(proximo[j] + [elemento])

        if possiveis:
            proximo[i] = min(possiveis, key=len)

    if proximo[-1] == False:
        return False
    return "".join(proximo[-1])


# In[3]:


if encontrar(palavra):
    print(palavra, "pode ser escrito como", encontrar(palavra))


# Exercício 185

# In[4]:


String = "AAAAAAAAAAAABBBBAAAAAACB"

lista = []
primeira_letra = String[0]
contador = 0

def rld(String):
    global lista
    global primeira_letra
    global contador
    
    if len(String)==0:
        lista.append(primeira_letra)
        lista.append(contador)
        return
    else:
        if String[0] == primeira_letra:
            contador += 1
            String = String[1:]
            return rld(String)
        else:
            lista.append(primeira_letra)
            lista.append(contador)
            primeira_letra = String[0]
            contador = 1
            String = String[1:]
            return rld(String)         



rld(String)
print(lista)

