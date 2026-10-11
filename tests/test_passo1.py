from chi_sono import NOME


def test_il_nome_e_stato_scritto():
    assert NOME.strip() != "", "Apri chi_sono.py e scrivi il tuo nome tra le virgolette"
