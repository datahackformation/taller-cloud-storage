# For loop and function

import time

def sumaCuadrado(param_list):
    a = param_list[0]
    b = param_list[1]
    return (a+b)**2

if __name__ == "__main__":

    iter_params = [(x, x+1) for x in range(10000)]
    results = list()

    start = time.time()

    for p in iter_params:
        results.append(sumaCuadrado(p))

    end = time.time()

    print('FIN DEL PROCESO EN FOR LOOP...')
    print('TIEMPO DE EJECUCION:', str(end-start))

