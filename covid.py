import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches

def moving_average(a, n=7) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

#dados

casos = [4,4,4,4,4,4,5,5,5,5,5,5,7,9,9,11,11,11,14,16,17,18,21,21,25,27,29,36,42,48,48,48,53,55,58,66,71,71,71,85,90,94,105,111,111,111,111,114,120,128,135,135,135,141,146,159,163,166,166,166,167,178,190,198,211,211,211,228,243,254,257,263,263,263,266,278]
mortes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,7,8,8,8,8,8]
recuperados =[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,4,4,4,4,4,5,5,5,8,8,8,9,15,18,19,21,21,21,23,29,31,33,47,47,47,47,52,60,68,80,80,80,81,89,91,95,99,99,99,102,108,112,115,121,121,121,129,129,135,139,149,149,149,154,191]
dias = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

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

#criação de informações para a legenda

string = 'Taxa de mortalidade: ' + str(taxa) + '%'
string2 = 'Casos ativos: ' + str(casos_ativos[len(casos_ativos)-1])

#criação dos arrays para plotagem

dias_mm = moving_average(dias)

x = np.arange(1,len(dias_mm)+1,1)
y_1 = moving_average(casos)
y_2 = moving_average(casos_dia)
y_3 = moving_average(recuperados)
y_4 = moving_average(mortes)
y_5 = moving_average(casos_ativos)

#plotagem do gráfico

blue_patch = mpatches.Patch(color='blue',label='Casos confirmados')
purple_patch = mpatches.Patch(color='purple',label='Casos ativos')
orange_patch = mpatches.Patch(color='orange',label='Casos diários')
green_patch = mpatches.Patch(color='green',label='Recuperados')
red_patch = mpatches.Patch(color='red',label='Óbitos confirmados')
taxa_patch = mpatches.Patch(color = 'white', label = string)
ativos_patch = mpatches.Patch(color = 'white', label = string2)

plt.plot(x,y_1,x,y_2,x,y_3,x,y_4,x,y_5)
dia = int(dias_mm[len(dias_mm)-1])
if dia < 10:
	string_dia = '0'+str(dia)
else:
	string_dia = str(dia)
plt.xlabel('Dias ( 04/06 - '+string_dia+'/08 )')
plt.grid(True)
plt.legend(handles=[blue_patch,purple_patch,red_patch,orange_patch,green_patch,taxa_patch,ativos_patch])
plt.show()
