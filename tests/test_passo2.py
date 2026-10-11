"""Passo 2. Leggi questo file come una specifica: ogni test descrive
con un esempio cosa deve restituire la funzione ottetti."""
from rete import ottetti


def test_ottetti_restituisce_quattro_elementi():
    assert len(ottetti("192.168.1.10")) == 4


def test_ottetti_sono_numeri_interi():
    # [192, 168, 1, 10] e ["192", "168", "1", "10"] NON sono la stessa cosa:
    # la prima e' una lista di numeri, la seconda una lista di testi.
    assert ottetti("192.168.1.10") == [192, 168, 1, 10]


def test_ottetti_di_un_altro_indirizzo():
    assert ottetti("10.0.0.254") == [10, 0, 0, 254]
