import threading

def executor_a(id=0):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteración {x}')

def executor_b(id=1):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteración {x}')

def executor_c(id=2):
    for x in range(0, 10):
        print(f'Hola, soy el Thread {id} iteración {x}')

#Hay tres maneras de mandar argumentos por parámetros
thread_a = threading.Thread(target=executor_a, args=[1]) #Lista
thread_b = threading.Thread(target=executor_b, args=(2,)) #Tupla
thread_c = threading.Thread(target=executor_c, kwargs={'id': 3}) #Dict

thread_a.start()
thread_b.start()
thread_c.start()