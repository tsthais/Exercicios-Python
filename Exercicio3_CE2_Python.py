#!/usr/bin/env python
# coding: utf-8

# **Lista 3**
# 
# Thaís Santos - 16/0145821
# 

# In[4]:


import random
    
def escolhe(matricula):
    random.seed(matricula) 
    cap1 = (2,8,9,11,12,15,16,18,20,21,22,24,26,27,28,30,31,32)
    cap2 = (36,40,44,45,46,48,50,51,53,55,56,57,59,60)
    cap3 = (63,64,65,68,71,72,74,76,78,80,81,84)
    return(random.sample(cap3, k=3))

 

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula")))


# Exercício 72

# In[11]:


99%3


# In[15]:


for i in range(1, 101):
    if i%3 == 0: 
        print("Número", i)
        print("Fizz")
        print(" ")
    elif i%5 == 0:
        print("Número", i)
        print("Buzz")
        print(" ")
    else: 
        print("Número", i)
        print(i)
        print(" ")


# Exercício 76

# In[77]:


string = input("Insira a string: ")


# In[78]:


string = string.replace(" ", "")
marcadores = "!´`@#$%^&*()_+<>?:.,;"
for j in string:
    if j in marcadores:
        string = string.replace(j, "")

# conda install unidecode
import unidecode
string = unidecode.unidecode(string)
        
string


# In[79]:


is_palindrome = True

for i in range(0, len(string) // 2):
  if string[i] != string[len(string) - i - 1]:
    is_palindrome =False

if is_palindrome:
  print(f"{string} is a palindrome ")
else:
  print(f"{string} is not palindrome")


# Exercício 81

# In[109]:


numero_binario = input("Insira o número binário: ")


# In[110]:


n = len(numero_binario)

i = 0

soma = 0 

while i < len(numero_binario):
    j = int(numero_binario[n-1])*(2**i)
    i = i+1
    n = n-1
    soma = soma + j
    
print(f"O número decimal equivalente é {soma}")

