import time
import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def stopwatch():
    counter = 0
    while counter != 20:
        time.sleep(1)
        counter += 1
        logging.info(f'Tiempo transcurrido: {counter} segundos')
        
        
def pow():
    counter = 0
    while counter != 40:
        time.sleep(0.5)
        counter += 1
        logging.info(f'{counter}^{counter}: {counter**counter}')
        
    
if __name__ == '__main__':
    thread_a = threading.Thread(target=stopwatch).start()
    thread_b = threading.Thread(target=pow).start()

'Acá se vé como dos threads distintos con tareas y tiempos distintos se ejecutan'