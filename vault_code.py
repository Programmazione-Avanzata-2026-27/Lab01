import random

# Costanti del gioco
CODICE_MIN = 1
CODICE_MAX = 50
TENTATIVI_BASE = 6
TENTATIVI_MIN = 3
MAX_LIVELLO = 3


def dai_indizio(tentativo, codice):
    """Restituisce un indizio confrontando il tentativo con il codice segreto"""
    if tentativo < codice:
        return "Più alto"
    else:
        return "Più basso"


def stampa_tentativi(n, usati):
    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""
    simboli = []
    for i in range(n): # 0 a 5
        if i < usati:
            simboli.append("X")
        else:
            simboli.append("O")

    for s in simboli:
        print(s, end=" ")
    print()


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore indovina il codice
    * False se il giocatore esaurisce i tentativi.

    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    n = TENTATIVI_BASE - livello
    if n < TENTATIVI_MIN:
        n = TENTATIVI_MIN

    # Codice da indovinare per questo livello
    codice = random.randint(CODICE_MIN, CODICE_MAX)
    # Numero di tentativi usati in quest livello finora
    usati = 0

    print()
    print(f"Livello {livello}) {n} tentativi")

    while usati < n:
        stampa_tentativi(n, usati)
        stringa = input("Tentativo: ")
        numero = int(stringa)

        if numero < CODICE_MIN or numero > CODICE_MAX:
            print(f"Il codice deve essere tra {CODICE_MIN} e {CODICE_MAX}")
            usati+=1
        elif numero == codice:
            print("Accesso consentito!")
            return True
        else: # Nell'intervallo ma non corretto
            usati+=1
            print(dai_indizio(numero, codice))

    print("GAME OVER: Tentativi esauriti!")
    return False

def main():
    print("=== Benvenuto in Vault Code ===")
    livello = 0

    while livello <= MAX_LIVELLO:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break


if __name__ == "__main__":
    main()
