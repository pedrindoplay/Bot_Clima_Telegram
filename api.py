import requests
import os
from dotenv import load_dotenv
load_dotenv()




def Clima(cidade):
    apiKey = os.environ.get("CLIMA")
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&lang=pt_br&units=metric&appid={apiKey}"


    requestt = requests.get(link)
    requesisao_dic = requestt.json()
    descricao = requesisao_dic['weather'][0]['description']
    pressao = requesisao_dic['main']['pressure']
    temp = requesisao_dic['main']['temp']
    umidade = requesisao_dic['main']['humidity']
    temp_arredondada = round(temp)

    return descricao, pressao, temp_arredondada, umidade


