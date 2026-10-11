"""Funzioni sugli indirizzi IPv4 (ripasso)."""


def ottetti(indirizzo):
    """Restituisce i quattro ottetti di un indirizzo IPv4 come numeri interi.

    Esempio: ottetti("192.168.1.10") deve restituire [192, 168, 1, 10]
    """
    # Passo 2: questa funzione contiene un errore. Trovalo e correggilo.
    parti = indirizzo.split(".")
    return parti


def e_valido(indirizzo):
    """Dice se una stringa e' un indirizzo IPv4 scritto correttamente.

    Un indirizzo e' valido se ha esattamente quattro parti separate da punti
    e ogni parte e' un numero intero compreso tra 0 e 255.
    """
    # Passo 3: questo controllo non basta. Completalo.
    parti = indirizzo.split(".")
    return len(parti) == 4


def indirizzo_di_rete(indirizzo, prefisso):
    """Sfida facoltativa: restituisce l'indirizzo di rete.

    Esempio: indirizzo_di_rete("192.168.1.130", 26) deve restituire "192.168.1.128"
    """
    raise NotImplementedError("Sfida facoltativa: scrivi tu questa funzione")
