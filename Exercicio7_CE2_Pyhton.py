#!/usr/bin/env python
# coding: utf-8

# **Lista de Exercícios 7**
# 
# 
# 
# Thaís da Silva Santos
# 
# 16/0145821

# In[9]:


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
    return(random.sample(cap7, k=3))

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula: ")))


# Exercício 160

# In[38]:


arquivo = open("words.txt", "r")
linhas = arquivo.readlines()
lista_ei = [" "]
lista_ie = [" "]


# In[39]:


for i in linhas:
    palavras = i
    for j in range(0, len(palavras)):
        if palavras[j].lower() == "e":
            if palavras[j+1].lower() == "i":
                if lista_ei[-1] != palavras:
                    lista_ei.append(palavras)
        if palavras[j].lower() == "i":
            if palavras[j+1].lower() == "e":  
                if lista_ie[-1] != palavras:
                    lista_ie.append(palavras)
            
        


# In[40]:


lista_ie = lista_ie[1:len(lista_ie)]
lista_ei = lista_ei[1:len(lista_ei)]


# In[41]:


print(f"O tamanho da lista com ie é {len(lista_ie)-1}")
print(f"O tamanho da lista com ei é {len(lista_ei)-1}")


# Exercício 164

# In[121]:


ano = int(input("Digite o ano desejado: "))

arquivo_meninos = str(ano)+"_BoysNames.txt"
arquivo_meninas = str(ano)+"_GirlsNames.txt"

import os

os.chdir("c:/Users/thais/Downloads/BabyNames")


# In[122]:


arquivo_meninos = open(arquivo_meninos, "r")
meninos = arquivo_meninos.readlines()

arquivo_meninas = open(arquivo_meninas, "r")
meninas = arquivo_meninas.readlines()


# Nomes de meninos:

# In[123]:


nomes_meninos = []
for i in meninos:
    palavras = i
    nomes_meninos.append(''.join(filter(str.isalpha, palavras)))


# In[115]:


nomes_meninos


# Nomes de meninas:

# In[124]:


nomes_meninas = []

for i in meninas:
    palavras = i
    nomes_meninas.append(''.join(filter(str.isalpha, palavras)))
    
        


# In[112]:


nomes_meninas


# In[133]:


nomes_neutros = []
for i in nomes_meninos:
    for j in nomes_meninas:
        if i == j:
            nomes_neutros.append(i)
            
if len(nomes_neutros) == 0:
    print("Não existem nomes neutros para esse ano.")
else: 
    print(f"Existem {len(nomes_neutros)} nomes de gênero neutro em {ano}.")
        


# Exercício 168

# In[186]:


for i in range(0, len(texto)-1):
    texto[i]= texto[i].split()


# In[187]:


for i in range(0, len(texto)-1):
    n_linha = i+1
    lista = texto[i]
    for j in range(0,len(lista)-2):
        if lista[j]==lista[j+1]:
            print(f"A palavra `{lista[j]}` se repete na linha {n_linha}")
        

