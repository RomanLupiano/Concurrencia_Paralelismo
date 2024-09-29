import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def new_process(time_to_sleep=0):
    logging.info('Comenzamos el proceso hijo!')

    time.sleep(time_to_sleep)

    logging.info('Terminamos el procesos hijo!')

def main():
    process = multiprocessing.Process(target=new_process,
                                        name='proceso-hijo',
                                        args=(1,),
                                        daemon=False)
    process.start()
    process.join()

    logging.info(f'Finalizamos el proceso principal')

if __name__ == '__main__':
    main()
