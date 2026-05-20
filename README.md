# 🔑 Kode Generator

Et simpelt Python-program med GUI til at generere koder.

## Krav

- Python 3.x
- `tkinter` 

## Sådan kører du det

```bash
python3 kode_generator.py
```

## Funktioner

- **Justerbar længde** - vælg mellem 4 og 64 tegn med en slider
- **Specialtegn** — valgfrit inkluder tegn som `!@#$%^&*`
- **Ekskluder tvetydige tegn** — fjerner tegn som `0`, `O`, `1`, `l`, `I` der er svære at skelne
- **Styrke-indikator** — viser om koden er Svag 🔴, Okay 🟡 eller Stærk 🟢
- **Kopierer automatisk** — koden kopieres til udklipsholderen ved generering
- **Historik** — gemmer de sidste 5 genererede koder med tidsstempel
- **Export** — gem historikken til `historik.txt`

## Filer

| Fil | Beskrivelse |
|-----|-------------|
| `kode_generator.py` | Hovedprogrammet |
| `historik.txt` | Oprettes automatisk når du eksporterer historik |
