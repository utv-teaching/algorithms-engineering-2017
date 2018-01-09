"""
    File name: mainFibonacci.py
    Author: Emanuele Vannacci
    Date created: 11/10/2016
    Date last modified: 14/10/2017
    Python Version: 2.7

    Il modulo contiene il main che ci permette di capire quale e' il
    calcolo che vogliamo effettuare e con quale algoritmo.

    Piu' precisamente viene processato il caso in cui l'input 
    proviene da riga di comando.
    Si esegue il calcolo, e si termina l'esecuzione.
"""

import sys
import fibonacci
import time


def recuperaAlgoritmo():
    """Permette di recuperare il numero dell'algoritmo passato come parametro
per riga di comando. Inoltre, effettua il controllo della validita' del dato."""
    alg = int(sys.argv[1]) #algoritmo che vogliamo eseguire
    if not(alg in (2, 3, 4)):
        print("Il numero di algoritmo deve essere 2, 3 o 4")
        return None    #istruzione superflua
    else:
        return alg


def recuperaNumero():
    """Permette di recuperare il numero di Fibonacci passato come parametro
per riga di comando. Inoltre, effettua il controllo della validita' del dato."""
    num = int(sys.argv[2])
    if num < 0:
        print("Il numero di Fibonacci da calcolare deve essere >= 0")
        return None  #istruzione superflua
    else:
        return num

def main():
    """Controlla il numero di argomenti che si sono passati per riga di
comando."""
    if len(sys.argv) == 3:
        algoritmo = recuperaAlgoritmo() #algoritmo che vogliamo eseguire
        numero = recuperaNumero() #il numero di fibonacci da calcolare
        if algoritmo != None and numero != None:
            inizio = time.clock()
            fib = fibonacci.calcolaFibonacci(algoritmo, numero)
            tempoTrascorso = time.clock() - inizio
            fibonacci.stampaRisultato(algoritmo, numero, fib, tempoTrascorso)
    else:
        print("""Avviare il programma con due argomenti:
Il numero che rappresenta l'algoritmo di Fibonacci scelto, ossia 2, 3 o 4.
Il numero di Fibonacci che si vuole calcolare.""")


if __name__ == '__main__':
    main()
