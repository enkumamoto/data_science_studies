import matplotlib.pyplot as plt

entrada = open("humano.fasta").read()
saida = open("humano.html","w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
    cont[entrada[k] + entrada[k+1]] += 1

# HTML

i = 1
for k in cont:
    transparencia = cont[k]/max(cont.values())
    transparencia = str(transparencia)
    saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0,0,255,"+transparencia+"')>"+k+"</div>")

    if i%4 == 0:
        saida.write("<div style='clear:both'></div>")
    i+=1

saida.close()
