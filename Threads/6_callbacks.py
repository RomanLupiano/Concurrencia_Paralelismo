#Los Callbacks son funciones que enviamos como argumentos para otras funciones
'''
def funcion_principal(callback):
    print("Ejecutando tarea principal")
    callback()  # Llamada al callback

def mi_callback():
    print("Tarea finalizada, ejecutando callback")

# Llamar a la función principal y pasarle el callback
funcion_principal(mi_callback)
'''

import logging
import requests
import threading

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def get_pokemon_name(response_json):
    name = response_json.get('forms')[0].get('name')
    logging.info(f'The pokemon is: {name}')
    
def get_name_random(response_json):
    name = response_json.get('results')[0].get('name').get('first')
    logging.info(f'The username is: {name}')
    
    
def error():
    logging.info('An error occurred')

    
def generate_request(url, success_callback, error_callback):
    response = requests.get(url)

    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()
        
        
if __name__ == '__main__':
    thread_a = threading.Thread(target=generate_request, kwargs={'url': 'https://pokeapi.co/api/v2/pokemon/1/', 
                                                                 'success_callback': get_pokemon_name,
                                                                 'error_callback': error})
    thread_a.start()
    
    thread_b = threading.Thread(target=generate_request, kwargs={'url': 'https://randomuser.me/api', 
                                                                 'success_callback': get_name_random,
                                                                 'error_callback': error})
    thread_b.start()
