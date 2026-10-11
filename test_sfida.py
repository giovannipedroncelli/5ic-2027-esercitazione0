"""Sfida facoltativa: non influisce sulla spunta verde."""
from rete import indirizzo_di_rete


def test_prefisso_24():
    assert indirizzo_di_rete("192.168.1.130", 24) == "192.168.1.0"


def test_prefisso_26():
    assert indirizzo_di_rete("192.168.1.130", 26) == "192.168.1.128"


def test_prefisso_20():
    assert indirizzo_di_rete("172.16.37.9", 20) == "172.16.32.0"


def test_prefisso_30():
    assert indirizzo_di_rete("10.0.0.7", 30) == "10.0.0.4"
