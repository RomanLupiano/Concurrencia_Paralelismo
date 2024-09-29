import logging

'''
Es mejor usar logging que prints
Con logging se pueden mandar 5 tipos de mensaje, cada uno con un nivel de prioridad
Critical (50)
Error (40)
Warning (30)
Info (20)
Debug (10)

Por defecto solo se ven los mensajes de prioridad >= 30, para eso se configura el basicConfig
'''


logging.basicConfig(
    level=logging.DEBUG,#Recibe integers logging.DEBUG es una constante que vale 10
    format='%(message)s - %(processName)s - %(filename)s - %(asctime)s - %(funcName)s - %(levelname)s - %(lineno)s', #Se puede agregar información a los mensajes modificando el format
    #filename='messages.txt' #Los mensajes se almacenarán en el archivo especificado
)

def mis_mensajes():
    logging.debug('Este es un mensaje de tipo Debug')
    logging.info('Este es un mensaje de tipo Info')
    logging.warning('Este es un mensaje de tipo Warning')
    logging.error('Este es un mensaje de tipo Error')
    logging.critical('Este es un mensaje de tipo Critical')

if __name__ == '__main__':
    mis_mensajes()