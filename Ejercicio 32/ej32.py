from datetime import datetime
import time
def reloj():
    while True:
        horas = datetime.now().hour
        minutos = datetime.now().minute
        segundos = datetime.now().second
        print(f"{horas}:{minutos}:{segundos}")
        time.sleep(1)

reloj()