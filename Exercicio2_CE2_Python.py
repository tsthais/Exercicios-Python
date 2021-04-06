#!/usr/bin/env python
# coding: utf-8

# **Lista de Exercícios 2**
# 
# 
# Thaís da Silva Santos - 16/145821
# 

# In[2]:


import random

 

def escolhe(matricula):
    random.seed(matricula)
    cap2 = (36,40,44,45,46,48,50,51,53,55,56,57,59,60)
    return(random.sample(cap2, k=3))

 

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula: ")))


# 1. Exercício 51

# In[32]:


a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
c = float(input("Qual é o valor de c? "))

from math import sqrt

discriminant = b**2-4*a*c

if discriminant < 0:
    print("Não existem raízes: discriminante < 0")
elif discriminant == 0:
    x = round((-b)/(2*a),2)
    print("Existe uma raiz: ", x)
else:
    x1 = round((-b + sqrt(discriminant))/(2*a),2)
    x2 = round((-b - sqrt(discriminant))/(2*a),2)
    print("Existem duas raízes: ", x1, " e,", x2)


# 2. Exercício 56

# In[57]:


rad = float(input("Qual é a frequência de radiação? "))

if rad < 3*(10**9):
    tipo = "Radio Waves"
elif 3*(10**9)<=rad< 3*(10**12):
    tipo = "Microwaves"
elif 3*(10**12) <= rad < 4.3*(10**14):
    tipo = "Infrared Light"
elif 4.3*(10**14) <= rad < 7.5*(10**14):
    tipo = "Visible Light"
elif 7.5*(10**14) <= rad < 3*(10**17):
    tipo = "Ultraviolet Light"
elif 3*(10**17) <= rad < 3*(10**19):
    tipo = "X- Rays"
elif 3*(10**19) <= rad:
    tipo = "Gamma Rays"
       
print("A radição pode ser classificada como",tipo)


# 3. Exercício 57

# In[70]:


minutos   = float(input("Quantos minutos em chamadas foram usados? "))
mensagens = int(input("Quantas mensagens foram enviadas? "))

if minutos <= 50 and mensagens <= 50:
    conta = 15+0.44
    cinco = 0.05*conta
    total = round(conta + cinco,2)
    print(f"O total da conta mensal foi de {total}")
elif minutos > 50 and mensagens <= 50:
    dif_minutos   = minutos - 50
    dif_mensagens = mensagens - 50
    
    custo_minutos   = 0.25*dif_minutos
    custo_mensagens = 0.15*dif_mensagens
    
    conta = 15+custo_minutos+custo_mensagens+0.44
    cinco = 0.05*conta
    total = round(conta + cinco,2)
    print(f"O adicional de minutos em chamada foram {dif_minutos}.")
    print(f"O total da conta mensal foi de {total}")

elif minutos <= 50 and mensagens > 50:
    dif_minutos   = minutos - 50
    dif_mensagens = mensagens - 50
    
    custo_minutos   = 0.25*dif_minutos
    custo_mensagens = 0.15*dif_mensagens
    
    conta = 15+custo_minutos+custo_mensagens+0.44
    cinco = 0.05*conta
    total = round(conta + cinco,2)
    print(f"O adicional de mensagens foi igual a {dif_mensagens}.")
    print(f"O total da conta mensal foi de {total}")

else:
    dif_minutos   = minutos - 50
    dif_mensagens = mensagens - 50
    
    custo_minutos   = 0.25*dif_minutos
    custo_mensagens = 0.15*dif_mensagens
    
    conta = 15+custo_minutos+custo_mensagens+0.44
    cinco = 0.05*conta
    total = round(conta + cinco,2)
    print(f"O adicional de minutos em chamada foram {dif_minutos} e o de mensagens foi igual a {dif_mensagens}.")
    print(f"O total da conta mensal foi de {total}")


    
    

