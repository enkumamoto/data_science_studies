import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]
z1 = [200,25,400,330,100] # Tamanho do marcador

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]
z2 = [100,330, 400, 25,200]

titulo = "Gráfico de dispersão 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Título
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1, y1, label = "Grupo 1", marker= "*", s=z1)
plt.scatter(x2, y2, label = "Grupo 2",marker= "*", s=z2)
plt.plot(x1, y1, label = "Grupo 1", linestyle= "--")
plt.plot(x2, y2, label = "Grupo 2", linestyle= "--")
plt.legend()
'''
aqui (quando descomentado) salvará a figura gerada pelo código. se quiser salvar a figura com algum nome, basta argumentar dentro dos parenteses. 
o formato png é a extensão padrão (para definir a qualidade da figura basta usar o argumento dpi=300 (ou a resolução desejada)).
também pode ser salvo em formato pdf, basta alterar a extensão
'''
# plt.savefig("figura 1.png. dpi=300")
# plt.savefig("figura1.pdf")
plt.show()
