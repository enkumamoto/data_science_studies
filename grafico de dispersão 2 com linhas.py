import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]
titulo = "Gráfico de dispersão 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Título
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1, y1, label = "Grupo 1")
plt.scatter(x2, y2, label = "Grupo 2")
plt.plot(x1, y1, label = "Grupo 1")
plt.plot(x2, y2, label = "Grupo 2")
plt.legend()
plt.show()