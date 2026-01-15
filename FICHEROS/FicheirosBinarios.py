import pickle
import datetime

data_hora=(datetime.datetime.now())
data, hora = str(data_hora).split()

amd = data.split("-")
hms = hora.split(":")

fecha_hora = {"ano":amd[0],
              "mes":amd[1],
              "dia":amd[2],
              "hora":hms[0],
              "minuto":hms[1],
              "segundo":hms[2]}

with open("data.dat","wb") as fichero:
    pickle.dump(fecha_hora, fichero)

with open("data.dat","rb") as fichero:
    dic = pickle.load(fichero)
    print(dic["hora"])
    print(dic["minuto"])
    print(dic["segundo"])
    print(dic["dia"])
    print(dic["mes"])
    print(dic["ano"])
