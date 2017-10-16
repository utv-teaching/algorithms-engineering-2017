"""
    File name: mainFibonacci.py
    Author: Emanuele Vannacci
    Date created: 11/10/2016
    Date last modified: 14/10/2017
    Python Version: 2.7

    Il modulo contiene il main che ci permette di capire di
    specificare il calcolo che vogliamo effettuare e con quale
    algoritmo.

    Piu' precisamente viene permesso l'inserimento di input
    interattivo da parte dell'utente. Ciclicamente si richiede il
    calcolo che l'utente vuole fare, lo si esegue, e poi si richiede
    le informazioni per svolgere un nuovo calcolo.
"""

import sys
import fibonacci
import time

def inserisciNumero():
    """Permette di inserire all'utente un numero di fibonacci valido"""
    num = int(raw_input("Inserisci il numero di Fibonacci da calcolare:\n"))
    while num < 0:
        num = int(raw_input("Inserisci un numero di Fibonacci valido (>= 0):\n"))
    return num

def inserisciAlgoritmo():
    """Permette di inserire all'utente un numero di fibonacci valido"""
    alg = int(raw_input("Scegliere l'algoritmo di fibonacci da eseguire (0, 2, 3, 4):\n"))
    while not(alg in (0, 2, 3, 4)):
        alg = int(raw_input("Scegliere un'opzione valida: 0 per uscire, 2,3 o 4 per\
calcolare Fibonacci con il relativo algoritmo:\n"))
    return alg


def main():
    """Permette di eseguire diversi calcoli di fibonacci con 3 diversi algoritmi."""
    if len(sys.argv) == 1:
        numero = inserisciNumero()
        algoritmo = inserisciAlgoritmo()
        while algoritmo != 0:
            inizio = time.clock()
            fib = fibonacci.calcolaFibonacci(algoritmo, numero)
            tempoTrascorso = time.clock() - inizio
            fibonacci.stampaRisultato(algoritmo, numero, fib, tempoTrascorso)
            numero = inserisciNumero()
            algoritmo = inserisciAlgoritmo()
        print("Hai deciso di uscire dal programma. Alla prossima! :)")
    else:
        print("""Eseguire il programma:
senza argomenti per avviare la sessione interattiva.""")

if __name__ == '__main__':
    main()


        
