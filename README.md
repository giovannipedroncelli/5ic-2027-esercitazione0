# Esercitazione 0 – Il tuo primo repository

Sistemi e Reti, classe quinta. Questa esercitazione **non è valutata**: serve a imparare il metodo di lavoro che useremo per tutto l'anno.

## Tre parole da conoscere

- **Repository (repo):** la cartella del progetto, conservata su GitHub insieme a tutta la sua storia.
- **Commit:** una fotografia del progetto in un certo momento, accompagnata da un messaggio che spiega cosa è cambiato e perché.
- **Test:** un piccolo programma che controlla se il tuo codice fa ciò che deve. Se il controllo riesce vedi una spunta verde, altrimenti una X rossa.

## Cosa c'è in questo repo

| File | A cosa serve | Lo modifichi? |
|---|---|---|
| `chi_sono.py` | Contiene il tuo nome | Sì (passo 1) |
| `rete.py` | Funzioni sugli indirizzi IPv4 | Sì (passi 2, 3 e sfida) |
| `tests/` | I test che controllano il tuo lavoro | **No, mai** |
| `sfida/` | I test della sfida facoltativa | **No, mai** |
| `conftest.py` | File di servizio per i test | **No, mai** |
| `.github/` e `.classroom50.yaml` | Fanno partire i test a ogni commit | **No, mai** |

## Come si lavora

1. Apri il file da modificare e clicca sulla matita in alto a destra.
2. Fai la modifica.
3. Clicca **Commit changes**, scrivi il messaggio e conferma.
4. Vai nella scheda **Actions**: dopo circa un minuto compare il risultato dei test, con una spunta verde o una X rossa. Clicca sull'ultima riga e apri il dettaglio per leggere quali test sono passati e quali no.

Un passo alla volta: **un commit per ogni passo**, non uno solo alla fine.

## I passi

### Passo 1 – Presentati
Apri `chi_sono.py` e scrivi il tuo nome e cognome tra le virgolette.
Fai il commit. In Actions vedrai ancora la X rossa: è normale, hai superato solo il primo test.

### Passo 2 – Trova il bug
Apri `tests/test_passo2.py` e **leggilo**: dice cosa deve restituire la funzione `ottetti`.
Poi apri `rete.py`: la funzione `ottetti` contiene un errore. Trovalo, correggilo, fai il commit.

### Passo 3 – Completa la funzione
La funzione `e_valido` controlla troppo poco: accetta anche indirizzi sbagliati.
Leggi `tests/test_passo3.py` per capire quali casi deve riconoscere, poi completala.
Guarda in Actions quali casi falliscono: ti dicono esattamente cosa manca.

### Passo 4 – La storia
Un ultimo test controlla che tu abbia fatto **almeno tre commit**. Se hai seguito i passi, è già verde.

### Sfida (facoltativa)
Scrivi la funzione `indirizzo_di_rete`. Il risultato della sfida si legge nel dettaglio in Actions, alla voce `sfida`, e non influisce sulla spunta verde.

## Le tre regole dei commit

1. **Piccoli e frequenti.** Un commit per ogni passo o per ogni correzione.
2. **Il messaggio dice cosa e perché.**
   - Sì: `Corretta ottetti: ora restituisce numeri interi`
   - No: `modifiche`, `fix`, `asdf`
3. **L'IA si dichiara.** Puoi usare un assistente IA, ma se lo fai aggiungi `[IA]` alla fine del messaggio.
   Esempio: `Completata e_valido con controllo 0-255 [IA]`

Ricorda: ti potrà essere chiesto di **spiegare a voce un tuo commit qualsiasi**. Se non sai spiegarlo, quel commit non vale, con o senza IA.

## Hai finito quando

- nella scheda **Actions** l'ultimo commit ha la spunta verde.

Non devi consegnare nulla: il docente vede già il tuo repo e il risultato dei test.
