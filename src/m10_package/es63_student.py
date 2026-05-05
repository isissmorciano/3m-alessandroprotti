

# ## Obiettivo

# - Organizzare funzioni correlate in moduli
# - Usare dizionari per rappresentare dati
# - Ordinare dati con criteri personalizzati usando `sorted()` e `key`

#Parte 3: Modulo `playlist.py`
    # Implementa funzioni per gestire collezioni di video.

    # **Funzioni di base:**
    # - `crea_playlist()` - crea un dizionario con nome e lista vuota di video
    # - `aggiungi_video()` - aggiunge un video alla playlist
    # - `rimuovi_video()` - rimuove un video per indice
    # - `durata_totale()` - somma le durate di tutti i video
    # - `dimensione_totale()` - somma le dimensioni di tutti i video
    # - `mostra_playlist()` - formatta la playlist in una stringa leggibile

    # **Funzioni di ordinamento (con sorted):**
    # - `ordina_per_durata()` - ordina i video dal più breve al più lungo
    #   - Usa `sorted()` con `key` per specificare quale attributo usare per l'ordinamento

    # **Approfondimento: sorted() con key**
    # `sorted()` ordina una lista. Normalmente ordina numeri e stringhe per valore naturale. Ma con `key`, puoi dire esattamente come confrontare gli elementi:
    # - `key=lambda v: v["durata"]` ordina usando il valore della chiave "durata"

    # ### Parte 4: Dati da usare

    # **Nome playlist:** `"Corso Python Base"`

    # **Video da aggiungere (nell'ordine):**

    # | Titolo | Durata (s) | Risoluzione | Bitrate (kbps) |
    # |--------|-----------|-------------|---|
    # | Introduzione a Python | 930 | 1080p | 5000 |
    # | Variabili e Tipi | 1335 | 720p | 3000 |
    # | Funzioni e Moduli | 1080 | 1080p | 5000 |
    # | Liste e Dizionari | 1560 | 480p | 2000 |

    # ### Parte 5: Utilizzo del Package
    # Scrivi uno script che:

    # 1. Importa il package
    # 2. Crea una playlist con il nome specificato
    # 3. Aggiunge i 4 video con i dati della tabella sopra
    # 4. Stampa la playlist originale
    # 5. Stampa la playlist ordinata per durata
    # 6. Stampa statistiche totali (durata e dimensione)


# from streaming import video ,playlist 

"""Esercizio 63: Utilizzo del package streaming con video e playlist."""

from streaming import video, playlist


def main() -> None:
    # Crea una playlist
    mia_playlist = playlist.crea_playlist("Corso Python 2026")

    # Crea i video con diverse risoluzioni e bitrate
    v1 = video.crea_video("Introduzione a Python", 930, "1080p", 5000)
    v2 = video.crea_video("Variabili e Tipi", 1335, "720p", 3000)
    v3 = video.crea_video("Funzioni e Moduli", 1080, "1080p", 5000)
    v4 = video.crea_video("Liste e Dizionari", 1560, "480p", 2000)
    v5 = video.crea_video("Introduzione OOP", 1350, "720p", 3000)

    # Aggiungi i video alla playlist
    playlist.aggiungi_video(mia_playlist, v1)
    playlist.aggiungi_video(mia_playlist, v2)
    playlist.aggiungi_video(mia_playlist, v3)
    playlist.aggiungi_video(mia_playlist, v4)
    playlist.aggiungi_video(mia_playlist, v5)

    # Stampa la playlist originale
    print("=" * 60)
    print("PLAYLIST ORIGINALE")
    print("=" * 60)
    print(playlist.mostra_playlist(mia_playlist))

    # Calcola statistiche
    durata_tot = playlist.durata_totale(mia_playlist)
    minuti_tot = durata_tot // 60
    secondi_tot = durata_tot % 60
    dimensione_tot = playlist.dimensione_totale(mia_playlist)

    print(f"\nDurata totale: {minuti_tot}:{secondi_tot:02d}")
    print(f"Dimensione totale: {dimensione_tot} MB")

    # Mostra i dimensioni di ogni video
    print("\nDimensioni dei video:")
    for v in mia_playlist["video"]:
        dim = video.dimensione_video(v)
        print(f"- {v['titolo']}: {dim} MB")

    # Ordina per durata
    print("\n" + "=" * 60)
    print("ORDINATI PER DURATA (crescente)")
    print("=" * 60)
    video_ordinati = playlist.ordina_per_durata(mia_playlist)
    print(playlist.mostra_playlist({"nome": "Ordinati per durata", "video": video_ordinati}))


if __name__ == "__main__":
    main()
         



