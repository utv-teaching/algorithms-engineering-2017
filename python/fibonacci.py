"""
    File name: fibonacci.py
    Author: Emanuele Vannacci
    Date created: 11/10/2016
    Date last modified: 11/10/2016
    Python Version: 2.7

    Il modulo contiene le versioni 2, 3, 4 dell'algoritmo di
    Fibonacci visto a lezione.
"""

def fibonacci2(num):
    """Permette di calcolare il num-esimo numero di fibonacci.
L'algoritmo proposto e' quello ricorsivo."""
    if num == 0:
        return 0
    elif num <=2:
        return 1
    else:
        return fibonacci2(num-1) + fibonacci2(num-2)

def fibonacci3(num):
    fib =[0, 1, 1]
    for i in range(3, num+1):
        fib.append(fib[i-1] + fib[i-2])
    #print(fib)
    return fib[num]

def fibonacci4(num):
    if num == 0:
        return 0
    temp1 = 1
    temp2 = 1
    for i in range(3, num+1):
        sum = temp1 + temp2
        temp2 = temp1
        temp1 = sum
    return temp1

def calcolaFibonacci(alg, num):
    """restituisce il numero di Fibonacci cercato eseguendo
l'algoritmo specificato dal valore del parametro alg."""
    if alg == 2:
        return fibonacci2(num)
    elif alg == 3:
        return fibonacci3(num)
    elif alg == 4:
        return fibonacci4(num)
    

def stampaRisultato(alg, num, ris, tempo):
    print("L'algoritmo fibonacci" + str(alg) + \
          "("+ str(num) +") ha restituito il valore", ris,\
          "in:\n", tempo, "secondi.\n")

#codice di test
if __name__ == "__main__":
    n = 14
    a = 2
    print(fibonacci2(n))
    print(fibonacci3(n))
    print(fibonacci4(n))
    print(calcolaFibonacci(a, n))

