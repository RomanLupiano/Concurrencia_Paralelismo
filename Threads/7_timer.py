import logging
import threading

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def callback():
    logging.info('Hola, soy un callback que no ejecuta de forma inmediata')

if __name__ == '__main__':
    thread = threading.Timer(3, callback) #Este thread va a esperar 3 segundos antes de ejecutarse
    thread.start()

    logging.info('Hola, soy el thread principal')
    logging.info('Estamos a la espera de la ejecución del callback') #Este se va a ejecutar en el thread principal y no va a esperar