"""
Praktische Aufgabe: Datei auslesen

Aufgabe:
Erstelle eine Textdatei mit dem Namen "text.txt" und folgendem Inhalt:

--- Inhalt von text.txt ---
Python ist eine vielseitige Programmiersprache.
Sie wird für Webentwicklung, Datenanalyse und KI verwendet.
Python ist einfach zu lernen.
--- Ende ---

Schreibe ein Python-Programm, das die Datei "text.txt" einliest
und den Inhalt zeilenweise ausgibt.

Bonus:
- Zähle die Anzahl der Wörter in der Datei.
- Gib die längste Zeile aus.
"""

from pathlib import Path

file_path = Path(__file__).parent / "text.txt"


def read_lines(file_path):
    """Liest den Inhalt einer Datei zeilenweise aus."""
    ...


def finde_wortanzahl(zeilen):
    """Zählt die Anzahl der Wörter in einer Liste von Zeilen."""
    ...


def finde_laengste_zeile(zeilen):
    """Findet die längste Zeile in einer Liste von Zeilen."""
    ...


# Gib den Inhalt zeilenweise aus
print("Inhalt der Datei:")

# Bonus 1: Zähle die Anzahl der Wörter
wortanzahl = finde_wortanzahl(...)
print("\nAnzahl der Wörter:", wortanzahl)


# Bonus 2: Finde die längste Zeile
laengste_zeile = finde_laengste_zeile(...)
