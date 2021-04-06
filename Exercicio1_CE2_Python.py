#!/usr/bin/env python
# coding: utf-8

# ### Lista 1 de Computação em Estatística 2

# **Thais da Silva Santos - 16/0145821**

#    

# Os exercícios selecionados foram o 22, 26 e 30.

# In[8]:


import random

def escolhe(matricula):
    random.seed(matricula)
    cap1 = (2,8,9,11,12,15,16,18,20,21,22,24,26,27,28,30,31,32)    
    return(random.sample(cap1, k=3))

 

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula: ")))


#    

# **1  Exercícios obrigatórios**
# 

# 1.1  Exercício 22
# 

# In the previous exercise you created a program that computed the area of a triangle when the length of its base and its height were known. It is also possible to compute the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3 be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle can be calculated using the following formula:

# In[17]:


s1 = float(input("Digite o valor de s1: "))
s2 = float(input("Digite o valor de s2: "))
s3 = float(input("Digite o valor de s3: "))
s  = (s1+s2+s3)/2


# In[37]:


import math

area = round(math.sqrt(s*(s-s1)*(s-s2)*(s-s3)), 4)

print("A área do triângulo é igual a", area)


#     

# 1.2  Exercício 26

# 
# Python’s time module includes several time-related functions. One of these is the asctime function which reads the current time from the computer’s internal clock and returns it in a human-readable format. Use this function to write a program that displays the current time and date. Your program will not require any input from the user.

# In[48]:


import time

time.asctime()


#     
#     

# 1.3  Exercício 30

# In[49]:


temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))


# In[56]:


temperatura_fah = (temperatura_celsius * 9/5) + 32
temperatura_kel = temperatura_celsius+273.15

print(f"A temperatura {temperatura_celsius}ºC é equivalente a {temperatura_fah}ºF e {temperatura_kel}K.")


#    
#   

# **2  Exercícios optativos**

# 2.1  Exercício 1

# Create a program that displays your name and complete mailing address. The address should be printed in the format that is normally used in the area where you live. Your program does not need to read any input from the user.

# In[58]:


print("Thaís da Silva Santos")
print("SMPW Quadra 3 Conjunto 3 Lote 2")


#    
#    

# 2.2  Exercício 2

# Write a program that asks the user to enter his or her name. The program should
# respond with a message that says hello to the user, using his or her name.

# In[59]:


nome = input("Qual é o seu nome?")
print(f"Olá {nome}")


#    

# 2.3  Exercício 3

# Write a program that asks the user to enter the width and length of a room. Once
# these values have been read, your program should compute and display the area of
# the room. The length and the width will be entered as floating-point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

# In[65]:


largura = float(input("Qual a largura da sala? "))
comprimento = float(input("Qual o comprimento da sala? "))
print(f"A área da sala é de {largura*comprimento}")


#   
#   

# 2.4 Exercício 4
# 

# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

# In[68]:


largura = float(input("Qual a largura do campo? "))
comprimento = float(input("Qual o comprimento do campo? "))

print(f"A área do campo é de {round((largura*comprimento)/43560, 3)} acres.")


#     
