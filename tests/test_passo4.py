"""Passo 4. Controlla la storia: servono almeno tre commit tuoi
che modificano chi_sono.py o rete.py."""
import subprocess
from pathlib import Path

import pytest

RADICE = Path(__file__).resolve().parent.parent
FILE = ["chi_sono.py", "rete.py"]


def git(*argomenti):
    return subprocess.run(["git", *argomenti], cwd=RADICE,
                          capture_output=True, text=True)


def test_almeno_tre_commit():
    if git("rev-parse", "--git-dir").returncode != 0:
        pytest.skip("Storia dei commit non disponibile")
    # Se e' stato scaricato solo l'ultimo commit, recupera il resto della storia.
    if git("rev-parse", "--is-shallow-repository").stdout.strip() == "true":
        if git("fetch", "--unshallow", "--quiet").returncode != 0:
            pytest.skip("Storia dei commit non disponibile")
    # Punto di partenza: il commit con cui Classroom 50 ti ha consegnato il repo.
    partenza = git("log", "--diff-filter=A", "--format=%H",
                   "--", ".classroom50.yaml").stdout.split()
    if partenza:
        conteggio = git("rev-list", "--count", f"{partenza[-1]}..HEAD", "--", *FILE)
    else:
        conteggio = git("rev-list", "--count", "--min-parents=1", "HEAD", "--", *FILE)
    commit = int(conteggio.stdout.strip())
    assert commit >= 3, (
        f"Hai fatto {commit} commit su chi_sono.py e rete.py: ne servono almeno 3, "
        "uno per ogni passo"
    )
