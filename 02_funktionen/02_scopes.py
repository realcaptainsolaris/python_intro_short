"""
Funktionen und Scopes in Python

Der Scope (Gültigkeitsbereich) bestimmt, wo Variablen definiert und verwendet
werden können. Python unterscheidet zwischen lokalem, globalem und
nicht-lokalem Scope. Das Verständnis von Scopes ist wichtig, um Funktionen
effektiv zu nutzen und Fehler durch unerwartete Variablenänderungen zu
vermeiden.

Themenübersicht:
1. Lokaler Scope
2. Globaler Scope
3. Die `global`-Anweisung
"""

# 1. Lokaler Scope
# Variablen, die innerhalb einer Funktion definiert werden, sind lokal
# und außerhalb der Funktion nicht sichtbar.


# print(local_var)  # Fehler: local_var ist außerhalb nicht definiert

# 2. Globaler Scope
# Variablen, die außerhalb von Funktionen definiert werden, sind global
# und können überall im Code verwendet werden.


# 3. Die `global`-Anweisung
# Mit der `global`-Anweisung kann innerhalb einer Funktion eine globale
# Variable verändert werden.
