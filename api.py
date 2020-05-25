import json
import requests

dicionarioPaises = {"sp":"http://worldtimeapi.org/api/timezone/america/Sao_Paulo", "ld":"http://worldtimeapi.org/api/timezone/europe/london","jp":"http://worldtimeapi.org/api/timezone/Asia/Tokyo" }
dicionario_horas = {}

for pais in dicionarioPaises:
    urlPais = dicionarioPaises[pais]
    requisincao = requests.get(urlPais)

    resposta_json = requisincao.json()

    dicionario_horas[pais] = int(resposta_json["datetime"][11:13])

def periodo_dia(hora) :
    print(hora)
    if hora >= 6 and hora <= 12 :  
        print("Esta de manhã")
    elif hora >= 13 and hora <= 17:
        print("Esta de tarde")
    else: 
        print("Esta a noite")

print("Horário de São Paulo")
periodo_dia(dicionario_horas["sp"])

print("Horário London")
periodo_dia(dicionario_horas["ld"])

print("Horário Chinaa")
periodo_dia(dicionario_horas["jp"])
