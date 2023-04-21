import matplotlib.pyplot as plt
# Aqui será gerado gráfico comparativo entre as barras

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]
titulo = "Gráfico em Barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Título
plt.title(titulo)

#Eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo 1") #o .plot gera gráficos em linhas o .bar em barras
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()
plt.show()