import requests
import threading

def get_name():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200: #OK

        results = response.json().get('results')
        name = results[0].get('name').get('first')

        print(name)

if __name__ == '__main__':
    for _ in range(0, 20):
        # Secuencial, manda el llamado a la API y espera a recibirlo para continuar con el for y mandar más peticiones
        get_name() 
        
        #Concurrente, no es necesario esperar a que el servidor responda para continuar con el for y mandar más peticiones
        thread = threading.Thread(target=get_name)
        thread.start()