import random

# Anzahl der Karten im Kartenspiel
anzahl_karten = 52


# Erstellt ein Kartendeck mit 52 Karten
def karten_mischen():
    karten = list(range(1, anzahl_karten + 1))
    return karten


# Zieht 5 zufällige Karten
def karten_ziehen():
    karten = karten_mischen()
    hand = random.sample(karten, 5)
    return hand


# Überprüft, ob man ein Paar hat
def ist_paar(hand):
    werte = []

    for karte in hand:
        wert = (karte - 1) % 13
        werte.append(wert)

    for wert in werte:
        if werte.count(wert) == 2:
            return True

    return False


# Überprüft, ob man einen Drilling hat
def ist_drilling(hand):
    werte = []

    for karte in hand:
        wert = (karte - 1) % 13
        werte.append(wert)

    for wert in werte:
        if werte.count(wert) == 3:
            return True

    return False


# Überprüft, ob man einen Vierling hat
def ist_vierling(hand):
    werte = []

    for karte in hand:
        wert = (karte - 1) % 13
        werte.append(wert)

    for wert in werte:
        if werte.count(wert) == 4:
            return True

    return False


# Überprüft, ob alle Karten die gleiche Farbe haben
def ist_flush(hand):
    farben = []

    for karte in hand:
        farbe = (karte - 1) // 13
        farben.append(farbe)

    if len(set(farben)) == 1:
        return True

    return False


# Überprüft, ob die Karten eine Straße bilden
def ist_strasse(hand):
    werte = []

    for karte in hand:
        wert = (karte - 1) % 13 + 2
        werte.append(wert)

    werte.sort()

    # Prüft, ob die Werte aufeinanderfolgen
    if werte == list(range(werte[0], werte[0] + 5)):
        return True

    # Sonderfall: Ass, 2, 3, 4, 5
    if werte == [2, 3, 4, 5, 14]:
        return True

    return False


# Gibt eine Karte als Text zurück
def karte_anzeigen(karte):
    werte = ["2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Bube", "Dame", "König", "Ass"]

    farben = ["Kreuz", "Pik", "Herz", "Karo"]

    wert = werte[(karte - 1) % 13]
    farbe = farben[(karte - 1) // 13]

    return wert + " " + farbe


# Zeigt alle gezogenen Karten an
def hand_anzeigen(hand):
    print("Deine Karten:")

    for karte in hand:
        print(karte_anzeigen(karte))


# Hauptprogramm
hand = karten_ziehen()

hand_anzeigen(hand)

print("Paar:", ist_paar(hand))
print("Drilling:", ist_drilling(hand))
print("Vierling:", ist_vierling(hand))
print("Flush:", ist_flush(hand))
print("Straße:", ist_strasse(hand))