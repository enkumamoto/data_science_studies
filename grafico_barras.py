import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,1,0]

titulo = "Gráfico em Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Título
plt.title(titulo)

#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y) #o .plot gera gráficos em linhas o .bar em barras
plt.show()