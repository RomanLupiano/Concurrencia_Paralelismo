import time
import threading

def codificar():
    time.sleep(2)

    print(f'Codificando')

def responder_correos():
    time.sleep(2)

    print(f'Respondiendo correos')

def realizar_calculos():
    time.sleep(2)

    print(f'Realizar los calculos')


threading.Thread(target=codificar).start()
threading.Thread(target=responder_correos).start()
threading.Thread(target=realizar_calculos).start()

