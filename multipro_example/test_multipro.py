# Multiprocessing and function

import multiprocessing as mp
import time

def sumaCuadrado(param_list):
    a = param_list[0]
    b = param_list[1]
    return (a+b)**2

if __name__ == "__main__":

    iter_params = [(x, x+1) for x in range(10000)]
    pool = mp.Pool(mp.cpu_count()-2)

    start = time.time()

    results = pool.map_async(sumaCuadrado, iter_params)
    pool.close()
    pool.join()

    end = time.time()

    print('FIN DEL PROCESO EN MULTIPROCESSING...')
    print('TIEMPO DE EJECUCION:', str(end-start))
