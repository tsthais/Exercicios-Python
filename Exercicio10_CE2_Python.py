#!/usr/bin/env python
# coding: utf-8

# **Exercícios 10**
# 
# Thaís da Silva Santos
# 
# 16/0145821

# In[1]:


import selenium
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[2]:


pasta = "C:/Users/thais/Documents/Ce2/chromedriver"


# In[3]:


driver = webdriver.Chrome(pasta)


# In[4]:


driver.maximize_window()


# Questão 01

# In[5]:


url = "https://www.worldometers.info/coronavirus/"


# In[6]:


driver.get(url)


# Data de atualização

# In[7]:


data = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[2]")
data.text


# Número de casos

# In[8]:


numeros = driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]/div/span')
total = []
for numeros in numeros:
    total.append(numeros.text)


# In[9]:


total[0]


# Número de mortes

# In[10]:


total[1]


# Número de casos ativos

# In[11]:


ativos = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[9]/div/div[2]/div/div[1]/div[1]')
ativos.text


# Questão 02

# In[12]:


url = "https://unb.br/graduacao/cursos"


# In[13]:


driver.get(url)


# In[14]:


cursos = driver.find_elements_by_xpath("//div[@class='item-page']/ul[@class='mb-4 pl-0']")


# In[15]:


for curso in cursos:
    print(curso.text)


# Questão 03

# In[16]:


url = "https://www.mercadolivre.com.br/"


# In[17]:


driver.get(url)


# In[23]:


item = input("O que você deseja encontrar no mercado livre? ")


# In[24]:


pesquisa = driver.find_element_by_xpath('/html/body/header/div/form/input')
pesquisa.clear()
pesquisa.send_keys(item)
pesquisa.send_keys(Keys.RETURN)


# In[25]:


card = driver.find_elements_by_css_selector("div.ui-search-result__content-wrapper")


# In[26]:


todos = []

for item in card:
    try:
        nomes = item.find_element_by_css_selector("h2.ui-search-item__group__element")
        precos = item.find_element_by_css_selector("span.price-tag-fraction")
        todos.append([nomes.text, precos.text])
    except:
        print("Erro")


# In[27]:


todos

