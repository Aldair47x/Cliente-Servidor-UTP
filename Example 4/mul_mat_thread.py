import time
import sys
import numpy as np
import random
import threading

def cell(res, matriz, i, j, n):
    suma = 0
    for k in range(n):
        suma += matriz[i,k] * matriz[k, j]
    res[i][j] = suma

def main():
    n = int(sys.argv[1])
    matriz = np.ones((n,n))
    res = np.zeros((n,n))

    start = time.time()
    for i in range(n):
        for j in range(n):
            threading.Thread(target=cell, args=(res, matriz, i, j, n)).start()
    end = time.time()
    print(end-start)
    with open("times thread", "a") as output:
        output.write('{} : {}\n'.format(n, end-start))

if __name__ == '__main__':
    main()
