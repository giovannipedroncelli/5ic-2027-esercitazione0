"""Passo 3. Ogni riga delle due tabelle e' un caso: prima gli indirizzi
che e_valido deve accettare, poi quelli che deve rifiutare."""
import pytest

from rete import e_valido


@pytest.mark.parametrize("indirizzo", [
    "192.168.1.10",
    "10.0.0.1",
    "0.0.0.0",
    "255.255.255.255",
])
def test_indirizzi_validi(indirizzo):
    assert e_valido(indirizzo) is True


@pytest.mark.parametrize("indirizzo", [
    "192.168.1",        # solo tre parti
    "192.168.1.10.5",   # cinque parti
    "192.168.1.256",    # 256 e' fuori dall'intervallo 0-255
    "300.1.1.1",        # 300 e' fuori dall'intervallo 0-255
    "192.168.1.abc",    # una parte non e' un numero
    "192.168..10",      # una parte e' vuota
    "192.168.1.-5",     # i numeri negativi non sono ammessi
])
def test_indirizzi_non_validi(indirizzo):
    assert e_valido(indirizzo) is False
