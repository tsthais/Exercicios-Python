#!/usr/bin/env python
# coding: utf-8

# Lista 6
# 
# Thaís da Silva Santos 
# 
# 16/0145821

# In[3]:


import random

def escolhe(matricula):
    random.seed(matricula)
    cap1 = (2,8,9,11,12,15,16,18,20,21,22,24,26,27,28,30,31,32)    
    cap2 = (36,40,44,45,46,48,50,51,53,55,56,57,59,60)
    cap3 = (63,64,65,68,71,72,74,76,78,80,81,84)
    cap4 = (85,86,87,89,91,92,94,97,99,101,103,104,106)
    cap5 = (111,115,117,118,119,122,123,124,126,127,131,132,133)
    cap6 = (138,139,140,141,144,147,148)
    return(random.sample(cap6, k=3))

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula")))


# Questão 140

# In[9]:


dicionario = {"A":"Newfoundland", "B": "Nova Scotia",
              "C": "Prince Edward Island", "E": "New Brunswick", 
              ("G", "H", "J"): "Quebec",
              ("K", "L", "M", "N", "P"):"Ontario", 
              "R": "Manitoba", "S": "Saskatchewan", "T": "Alberta", 
              "V": "British Columbia", "X": "Nunavut", 
              "X": "Northwest Territories", "Y": "Yukon"}


# In[52]:


cod_postal = input("Qual é o seu código postal? ")

primeira_letra = cod_postal[0]
numero = int(cod_postal[1])

    
if (primeira_letra in dicionario) and numero != 0:
    print("O código postal é urbano e de", dicionario.get(primeira_letra))
elif (primeira_letra in dicionario) and numero == 0:
    print("O código postal é rural e de", dicionario.get(primeira_letra))
else:
    print("Código postal inválido")


# Questão 141

# In[87]:


centena = {1: "cento", 2: "duzentos", 3: "trezentos",
          4: "quatrocentos", 5: "quinhentos", 6: "seiscentos", 
          7: "setecentos", 8: "oitocentos", 9: "novecentos"}
dezena = {2: "vinte", 3: "trinta",
          4: "quarenta", 5: "cinquenta", 6: "sessenta", 
          7: "setenta", 8: "oitenta", 9: "noventa"}
unidade = {1: "um", 2: "dois", 3: "três",
          4: "quatro", 5: "cinco", 6: "seis", 
          7: "sete", 8: "oito", 9: "nove"}
dezena1 = {11: "onze", 12: "doze", 13: "treze", 
          14: "quartoze", 15: "quinze", 16: "dezesseis", 
          17: "dezessete", 18: "dezoito", 19: "dezenove"}
dezena2 = {10: "dez", 20: "vinte", 30: "trinta", 
          40: "quarenta", 50: "cinquenta", 60: "sessenta", 
          70: "setenta", 80: "oitenta", 90: "noventa"}
centena1 = {1: "cem", 2: "duzentos", 3: "trezentos",
          4: "quatrocentos", 5: "quinhentos", 6: "seiscentos", 
          7: "setecentos", 8: "oitocentos", 9: "novecentos"}


# In[99]:


valor = (input("Digite o valor:"))


# In[100]:


pr_numero = int(valor[0])
sg_numero = int(valor[1])
tr_numero = int(valor[2])


if (pr_numero in centena) and sg_numero != 1 and tr_numero !=0:
    print(centena.get(pr_numero),"e", dezena.get(sg_numero),"e",  unidade.get(tr_numero))
elif (pr_numero in centena) and sg_numero == 1 and tr_numero != 0:
    numero = int(valor[1:3])
    print(centena.get(pr_numero),"e", dezena1.get(numero))
elif (pr_numero in centena)  and sg_numero >= 1 and tr_numero == 0:
    numero = int(valor[1:3])
    print(centena.get(pr_numero),"e", dezena2.get(numero))
elif (pr_numero in centena) and sg_numero == 0 and tr_numero == 0:
    print(centena1.get(pr_numero))
else:
    print("O valor é inválido")

