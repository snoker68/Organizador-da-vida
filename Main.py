import argparse
from datetime import datetime


input ("Escreva sua prioridade!!!")
print ("Certo seu voce tem uma obrigação agendada")

def verficar_Data (data_str): 
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        print(f"A data {data_str} foi resevada no seu calendario")
        return data
    except ValueError:
        print(f"data incorreta {data_str} ela esta incorreta")
        return None


data =  input("digita data do seu compromisso e a hora (precisa ser nesse formato DD/MM/AAAA)")
verficar_Data (data),