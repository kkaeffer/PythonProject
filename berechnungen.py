# Klasse Berechnungen
class Berechnungen:

    # Speichert die Daten und Festlegung der gesamt ECTS
    def __init__(self, daten, gesamt_ects=180):
        self.daten = daten
        self.gesamt_ects = gesamt_ects

    # Berechnung aller ECTS der bestandenen Module für die Fortschrittsanzeige
    def erreichte_ects_berechnen(self):
        erreichte_ects = 0

        for zeile in self.daten:
            if zeile["Bestanden"].strip().lower() == "ja":
                erreichte_ects += float(zeile["ECTS"])

        return erreichte_ects

    # Berechnung der noch übrig gebliebenen ECTS
    def rest_ects_berechnen(self):
        self.erreichte_ects = self.erreichte_ects_berechnen()

        return max(self.gesamt_ects - self.erreichte_ects, 0)

    # Auslesen aller bisher erhaltenen Noten und ignoriert Module ohne Note
    def noten_holen(self):
        noten = []

        for zeile in self.daten:
            note = zeile["Note"].strip()

            if note.upper() != "K.A.":
                noten.append(float(note))

        return noten

    # Berechnung des Notendurchschnittes
    def notendurchschnitt_berechnen(self):
        noten = self.noten_holen()

        if noten:
            return sum(noten) / len(noten)

        return 0

    # Festlegung der Farbe des Achtecks anhand des Notendurchschnittswert
    def farbe_achteck_berechnen(self):
        notendurchschnitt = self.notendurchschnitt_berechnen()

        if notendurchschnitt <= 2.00:
            return "#4CAF50"
        elif notendurchschnitt <= 2.5:
            return "#FFFF33"
        else:
            return "#FF0000"

    # Auslesen aller Module und dazugehörigen Notenstand, erstellung Notenliste
    def noten_liste_erstellen(self):
        noten_liste = []

        for zeile in self.daten:
            noten_liste.append({
                "Modul": zeile["Modul"],
                "Note": zeile["Note"]
            })

        return noten_liste