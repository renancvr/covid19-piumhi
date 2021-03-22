import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import math

def moving_average(a, n=7) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


#leitura de dados e montagem dos arrays para plotagem:
df = pd.read_excel('dados.xlsx')

casos = []
mortes = []
recuperados = []
dias = []

for i in range(len(df.values)):
    casos.append(df.values[i][1])
    mortes.append(df.values[i][2])
    recuperados.append(df.values[i][3])
    dias.append(df.values[i][4])

#calculo de casos diários 
casos_dia = [0]

for i in range(len(casos)):
	if i+1<=len(casos)-1:
		novos_casos = casos[i+1] - casos[i]
		casos_dia.append(novos_casos)

#calculo de casos ativos
casos_ativos = []

for i in range(len(casos)):
	ativos = (casos[i] - recuperados[i]) - mortes[i]
	casos_ativos.append(ativos)

#atualizar a tabela de dados com casos diários e casos ativos
dados_atualizados = [casos,mortes,recuperados,dias,casos_dia,casos_ativos]

df = pd.DataFrame(dados_atualizados,index=['Casos Confirmados','Óbitos','Recuperados','Dia','Casos Diários','Casos Ativos']).T
df.to_excel('dados.xlsx')

#cálculo taxa de mortalidade
taxa = round((mortes[len(mortes)-1] * 100) / casos[len(casos)-1],2)


#criação de informações para a legenda
string_mortalidade = 'Taxa de mortalidade: ' + str(taxa) + '%'
string_ativos = 'Casos ativos: ' + str(int(casos_ativos[len(casos_ativos)-1]))
string_mortes = 'Total de mortes: ' + str(mortes[len(mortes)-1])

#calcular número R
r = math.exp((math.log(34691/((1/(casos[len(casos)-1]/(casos[0]*34691)))-1)))/(len(dias)))
print('Número R: ' + str(r))

#criação dos arrays para plotagem
y_casos = moving_average(casos)
y_casos_dia = moving_average(casos_dia)
y_recuperados = moving_average(recuperados)
y_mortes = moving_average(mortes)
y_casos_ativos = moving_average(casos_ativos)
x = np.arange(1,len(y_casos)+1,1)


#plotagem do gráfico
f1 = plt.figure(1)
blue_patch = mpatches.Patch(color='blue',label='Casos confirmados')
purple_patch = mpatches.Patch(color='purple',label='Casos ativos')
green_patch = mpatches.Patch(color='green',label='Recuperados')
taxa_patch = mpatches.Patch(color = 'white', label = string_mortalidade)
ativos_patch = mpatches.Patch(color = 'white', label = string_ativos)

legenda = 'Dias (04/06/2020 - '+str(int(dias[len(dias)-1]))+'/03/2021 )'

plt.plot(x,y_casos,color='blue')
plt.plot(x,y_recuperados,color='green')
plt.plot(x,y_casos_ativos,color='purple')

plt.ylabel('Média móvel de 7 dias')

plt.xlabel(legenda)
plt.grid(True)
plt.legend(handles=[blue_patch,purple_patch,green_patch,taxa_patch,ativos_patch])

f2 = plt.figure(2)
orange_patch = mpatches.Patch(color='orange',label='Casos diários')
red_patch = mpatches.Patch(color='red',label='Óbitos confirmados')
mortes_patch = mpatches.Patch(color='white',label=string_mortes)

plt.plot(x,y_mortes,color='red')
plt.plot(x,y_casos_dia,color='orange')

plt.ylabel('Média móvel de 7 dias')

plt.xlabel(legenda)
plt.grid(True)
plt.legend(handles=[red_patch,orange_patch,taxa_patch,mortes_patch])

plt.show()