import csv
import json

datos = {"nome": "Jose", "edad": 30, "xenero": "Home"}
with open ("exemplo.json",'w') as ficheiro:
    json.dump(datos,ficheiro)

with open("exemplo.json",'r') as ficheiro:
    datJson = json.load(ficheiro)
    print(datJson)
    print(type(datJson))

with open("exemplo.csv",'a', newline='') as ficheiro:
    writer = csv.writer(ficheiro)
    writer.writerow(datJson.values())