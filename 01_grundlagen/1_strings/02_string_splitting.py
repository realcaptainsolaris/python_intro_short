"""
String Splitting in Python

Das Zerlegen von Strings (String Splitting) ist eine häufige Aufgabe in der
Datenverarbeitung. Python bietet verschiedene Methoden, um Strings anhand
von Trennzeichen oder festgelegten Mustern zu zerlegen.

Themenübersicht:
1. Die Methode `split()`
2. Zerlegen mit benutzerdefinierten Trennzeichen
3. Zerlegen mit maximaler Anzahl von Teilen
"""

import re

# 1. Die Methode `split()`
# `split()` zerlegt einen String standardmäßig anhand von Leerzeichen.

text = "Dies ist ein Beispieltext"
# Ausgabe: ['Dies', 'ist', 'ein', 'Beispieltext']

# 2. Zerlegen mit benutzerdefinierten Trennzeichen
# Ein Trennzeichen kann als Argument an `split()` übergeben werden.
csv_text = "Name,Alter,Beruf"

# 3. Zerlegen mit maximaler Anzahl von Teilen
# Mit dem zweiten Argument von `split()` kann die maximale Anzahl der
# Zerlegungen festgelegt werden.
