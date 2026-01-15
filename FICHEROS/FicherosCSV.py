import csv

with open('exemplo.csv','w') as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow(['Nome','Edade','Xénero'])
    writer.writerow(['Pedro','23','Home'])
    writer.writerow(['Rosa','25','Muller'])

with open('exemplo2.csv','w') as ficheiro:
    ficheiro.writelines("Nome"+','+'Edade'+','+'Xénero'+'\n')
    ficheiro.writelines("Pedro"+','+'23'+','+'Home'+'\n')
    ficheiro.writelines("Rosa"+','+'25'+','+'Muller')

with open('exemplo.csv','r') as ficheiro:
    reader = csv.reader(ficheiro)
    for fila in reader:
        print(fila)