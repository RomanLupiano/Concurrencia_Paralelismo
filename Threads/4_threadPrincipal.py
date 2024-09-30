import logging
import threading


logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s - %(thread)s %(threadName)s - %(filename)s - %(asctime)s:  %(message)s'
)

def task():
    for x in range(0, 3):
        logging.debug('Notar la diferencia entre el thread principal y los generados')

if __name__ == '__main__':
    thread_a = threading.Thread(target=task)
    thread_b = threading.Thread(target=task)
    thread_c = threading.Thread(target=task)

    thread_a.start()
    thread_b.start()
    thread_c.start()
    task()





