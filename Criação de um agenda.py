from icalendar import Calendar, Event,Alarm
from datetime import  datetime,timedelta

titulo = input("Digite nome do evento:")
descricao = input("Descreva seu evento")

data_inicio_str = input("Digite data e a hora do inicio do evento:")
data_inicio = datetime.strftime(data_inicio_str, "%d/%m/%y %H:%M")

data_termino_str = input("Digite data e a hora do termino do evento:")
data_termino = datetime.strftime(data_termino_str, "%d/%m/%y %H:%M")

Notificação = int(input("informe quanto minutos voce gostaria de sempre lembrado antes do evento:"))


calendario = Calendar()

evento =Event()
evento.add('summary', titulo)
evento.add('description', descricao)
evento.add('dtstart', data_inicio)
evento.add('dtend', data_termino)

lembrete = Alarm()
lembrete.add('action', 'Display')
lembrete.add('description', "lembrete: " + titulo)
lembrete.add('trigger', timedelta(minutes=-Notificação))

evento.add_component(evento)

calendario.add_component(evento)

nome_arquivo = input("digite nome do arquivo para salvar") + ".ics"
with open(nome_arquivo,'wb') as f:
    f.write(calendario.to_ical())

print(f"Seu evento foi agendado com nome {nome_arquivo}.a arquivo gerado com sucesso")