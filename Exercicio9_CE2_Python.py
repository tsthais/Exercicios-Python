#!/usr/bin/env python
# coding: utf-8

# **Exercício 9**
# 
# Thaís Santos 
# 
# 16/0145821

# In[1]:


import pandas as pd


# In[2]:


endereco = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-31-2020.csv"


# In[3]:


dados = pd.read_csv(endereco)


# O conjunto de dados tem 3.979 linhas e 14 colunas

# In[4]:


dados.shape


# As primeiras 5 cincos do banco de dados são:

# In[5]:


dados.head()


# As últimas 5 linhas do conjunto de dados são:

# In[6]:


dados.tail()


# Existem informações sobre a Covid- 19 para 191 países

# In[7]:


paises = dados.Country_Region.unique()
len(paises)


# Os 10 países com maior número de morte são:

# In[8]:


paises = dados.groupby("Country_Region")


# In[9]:


paises.sum().sort_values("Deaths", ascending = False)[["Deaths"]][0:10]


# Os 10 países com maiores taxas de recuperação são:

# In[10]:


paises.sum().sort_values("Recovered", ascending = False)[["Recovered"]][0:10]


# Os paises sem registro de morte são:

# In[11]:


sem_morte = paises.sum().sort_values("Deaths")[["Deaths"]]

sem_morte.loc[sem_morte["Deaths"] == 0]


# O número médio de mortes no Brasil é de 7.220,33.

# In[12]:


brasil = dados.loc[dados["Country_Region"] == "Brazil"]


# In[13]:


media_mortes_brasil = round(brasil["Deaths"].mean(), 2)
print(media_mortes_brasil)


# Os estados brasileiros que tem número médio de mortes maior do que a média brasileira são:

# In[27]:


estados_brasil = brasil.groupby("Province_State")


# In[28]:


estados_brasil = estados_brasil.mean()


# In[29]:


estados_brasil.loc[estados_brasil["Deaths"] > media_mortes_brasil].sort_values("Deaths", ascending = False)[["Deaths"]]


# Os estados brasileiros que tem número médio de mortes menor do que a média brasileira são:

# In[30]:


estados_brasil.loc[estados_brasil["Deaths"] < media_mortes_brasil].sort_values("Deaths", ascending = False)[["Deaths"]]


# Os países que apresentam apenas informações gerais são:

# In[31]:


sem_estados = dados[dados['Province_State'].isnull()]


# In[32]:


sem_estados.groupby(["Country_Region"]).groups.keys()


# Dos países que só apresentam informações gerais, o que tem maiores números de morte são:

# In[33]:


sem_estados.groupby(["Country_Region"]).sum().sort_values("Deaths", ascending = False)[["Deaths"]][0:3]


# O número de morte nos últimos 5 dias de 2020 foi de 8.985.607

# In[34]:


dia26 = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-26-2020.csv")
dia27 =  pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-27-2020.csv")
dia28 =  pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-28-2020.csv")
dia29 =  pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-29-2020.csv") 
dia30 =  pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-30-2020.csv")
dia31 =  pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-31-2020.csv")


# In[35]:


dados = [dia26, dia27, dia28, dia29, dia30, dia31]
mortes = [0,0,0,0,0,0]
i=0

while i < len(dados):
    mortes[i] = dados[i]["Deaths"].sum()
    i = i+1
    
sum(mortes[1:6])

