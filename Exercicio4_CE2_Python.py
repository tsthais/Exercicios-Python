#!/usr/bin/env python
# coding: utf-8

# **Lista de exercícios 4**
# 
# Thaís da Silva Santos 
# 
# 16/0145821

# In[449]:


import random

 

def escolhe(matricula):
    random.seed(matricula)
    cap1 = (2,8,9,11,12,15,16,18,20,21,22,24,26,27,28,30,31,32)    
    cap2 = (36,40,44,45,46,48,50,51,53,55,56,57,59,60)
    cap3 = (63,64,65,68,71,72,74,76,78,80,81,84)
    cap4 = (85,86,87,89,91,92,94,97,99,101,103,104,106)
    return(random.sample(cap4, k=3))

 

print("Você deverá entregar os exercícios: ", escolhe(input("Escreva o número de sua matricula")))


# Exercício 92

# In[437]:


def dia_do_ano(dia, ano):
    if ano % 4 == 0:
        Bx = [31,29,31,30,31,30,31,31,30,31,30,31]
        
        Meses = ["01", "02", "03", "04", "05", 
        "06", "07", "08", "09", "10", 
        "11", "12"]
        
        x = []
        for j in range(len(Bx)):
            x.append(sum(Bx[:j+1]))
            
        dias = []
        for i in range(1,367):
            dias.append(i)
            
        lista = [[1,31]]
        for i in range(1,len(x)):
            lista.append([x[i-1]+1, x[i]])
            
        intervalo = 0
        
        if 31 >= dia >= 1:
            return(f"{dia}/01")
        else:
            for j in range(0,len(lista)): 
                if lista[j][1] >= dia >= lista[j][0]: 
                    intervalo = j
            a = lista[intervalo]
            dias_mes = []
            dias_mes.extend(dias[a[0]:dia])
            mes_aux = Meses[intervalo]
            return(f"{len(dias_mes)+1}/{mes_aux}")
    else:
        Bx = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        Meses = ["01", "02", "03", "04", "05", 
        "06", "07", "08", "09", "10", 
        "11", "12"]
        
        x = []
        for j in range(len(Bx)):
            x.append(sum(Bx[:j+1]))
            
        dias = []
        for i in range(1,367):
            dias.append(i)
            
        lista = [[1,31]]
        for i in range(1,len(x)):
            lista.append([x[i-1]+1, x[i]])
            
        intervalo = 0
        
        if 31 >= dia >= 1:
            return(f"{dia}/01")
        else:
            for j in range(0,len(lista)): 
                if lista[j][1] >= dia >= lista[j][0]: 
                    intervalo = j
            a = lista[intervalo]
            dias_mes = []
            dias_mes.extend(dias[a[0]:dia])
            mes_aux = Meses[intervalo]
            return(f"{len(dias_mes)+1}/{mes_aux}")
        


# In[439]:


print(dia_do_ano(59,2019))
print(dia_do_ano(60,2020)) #ano bissexto


# In[448]:


# semestre 2020.2
# início: 1 de fevereiro
# 90 dias de aula

import datetime

inicio = "01/02/2021"
formato = '%d/%m/%Y'
dt = datetime.datetime.strptime(inicio, formato)

tt = dt.timetuple()
inicio_ord = tt.tm_yday

feriados_fds     = 19
dias_letivos     = 90

fim = inicio_ord + dias_letivos + feriados_fds
final_semestre = (f"{dia_do_ano(fim, 2021)}/2021")

print(f'O semestre 2020.2 tem início em {inicio} e termina em {final_semestre}.')


# Exercício 97

# In[464]:


def prec(operador):
    if operador == "+" or operador == '-':
        return(1)
    elif operador == "*" or operador == "/":
        return(2)
    elif operador == "^":
        return(3)
    else:
        return(-1)


# In[509]:


def main():
    operador = input("Digite seu operador: ")
    if operador == "+" or operador == '-' or operador == "*" or operador == "/" or operador == "^":
        print(f"Seu operador é {operador} de precedência {prec(operador)}.")
    else:
        print("Sua entrada não é um operador válido.")
main()


# Exercício 103

# In[582]:


# Exercicio 100

import random

def senha_aleatoria():

    comprimento = random.randint(7,10)

    senha = ""
    for i in range(comprimento):
        caracter = chr(random.randint(33,126))
        senha += caracter

    return senha
    
def main():
    print("Sua senha aleatória é:", senha_aleatoria())

main()


# In[589]:



# Exercicio 102

def validade():
    while True:
        senha_ale = senha_aleatoria()
        if len(senha_ale) < 8:
            print("Atenção: Sua senha tem menos de 8 dígitos.")
        if not any(k.isdigit() for k in senha_ale):
            print("Atenção: Sua senha não tem números.")
        if not any(j.isupper() for j in senha_ale):
            print("Atenção: Sua senha não tem letras maiúsculas.")
        if not any(l.islower() for l in senha_ale):
            print("Atenção: Sua senha não tem letras minúsculas.")
        else:
            print("Parabéns! Sua senha é válida.") 
            print(f'Sua senha válida é {senha_ale}.')
            break
validade()


# In[749]:


# exercicio 103

def contador():
    contador = 0
    while True:
        senha_ale = senha_aleatoria()
        contador = contador + 1
        if len(senha_ale) >= 8:
            if any(k.isdigit() for k in senha_ale):
                if any(j.isupper() for j in senha_ale):
                    if any(l.islower() for l in senha_ale):
                        print(f"O número de tentativas necessárias para uma senha válida foi de {contador}.")
                        print(f"Sua senha é {senha_ale}.")
                        break
contador()

