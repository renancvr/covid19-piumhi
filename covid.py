import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches

#dados

casos = [4,4,4,4,4,4,5,5,5,5,5,5,7,9,9,11,11,11,14,16,17,18,21,21,25,27,29,36,42,48,48,48,53,55,58,66,71,71,71,85,90,94]
mortes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4]
recuperados =[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,4,4,5,5,5,8,8,8,9,15,18,19,21,21,21,23,29,31]
dias = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#cálculo de casos diários

casos_dia = [0]

for i in range(len(casos)):
	
	if i+1<=len(casos)-1:
		novos_casos = casos[i+1] - casos[i]
		casos_dia.append(novos_casos)

#cálculo de casos ativos

casos_ativos = []

for i in range(len(casos)):
	
	ativos = casos[i] - recuperados[i]
	casos_ativos.append(ativos)

#cálculo taxa de mortalidade

taxa = round((mortes[len(mortes)-1] * 100) / casos[len(casos)-1],2)
string = 'Taxa de mortalidade: ' + str(taxa) + '%'

#criação dos arrays para plotagem

x = np.arange(1,len(dias)+1,1)
y_1 = np.array(casos)
y_2 = np.array(casos_dia)
y_3 = np.array(recuperados)
y_4 = np.array(mortes)
y_5 = np.array(casos_ativos)

#plotagem do gráfico

blue_patch = mpatches.Patch(color='blue',label='Casos confirmados')
purple_patch = mpatches.Patch(color='purple',label='Casos ativos')
orange_patch = mpatches.Patch(color='orange',label='Casos diários')
green_patch = mpatches.Patch(color='green',label='Recuperados')
red_patch = mpatches.Patch(color='red',label='Óbitos confirmados')
taxa_patch = mpatches.Patch(color = 'white', label = string)

plt.plot(x,y_1,x,y_2,x,y_3,x,y_4,x,y_5)
dia = dias[len(dias)-1]
plt.xlabel('Dias ( 04/06 - '+str(dia)+'/07 )')
plt.grid(True)
plt.legend(handles=[blue_patch,purple_patch,red_patch,orange_patch,green_patch,taxa_patch])
plt.show()
