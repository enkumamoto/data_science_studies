# Estudo de caso do crescimento da população brasileira entre 1980-2016
import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x=[]
y=[]

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.bar(x, y, color="#33fff9")
plt.plot(x, y, color='r', linestyle="--")

plt.title("Crescimento da população brasileira entre 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()