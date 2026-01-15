import datetime

ficheiro = open('/home/dam/salida.txt')

for linha in ficheiro:
    print(linha)

ficheiro.close()

data_hora= (datetime.datetime.now())
data, hora =str(data_hora).split()

ficheiro2 = open('saudo.txt','w')

ficheiro2.write("Hola, soy Juan\n")
ficheiro2.write(data)
ficheiro2.write('\n')
ficheiro2.write(hora)
ficheiro2.write('\n')
ficheiro2.write("Acabo y cierro fichero")

ficheiro2.close()

ficheiro2 = open ('saudo.txt','r')
lectura = ficheiro2.read()

ficheiro2.close()
