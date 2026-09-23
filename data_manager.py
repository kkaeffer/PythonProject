import csv

# Klasse DatenManager für das Einlesen der CSV-Datei
class DatenManager:

    # Speichert den Dateinamen und erstellt eine leere Datenliste
    def __init__(self, dateiname):
        self.dateiname = dateiname
        self.daten = []

    # Liest die Daten aus der CSV-Datei ein
    def daten_einlesen(self):
        with open(self.dateiname, mode="r", encoding="utf-8") as datei:
            reader = csv.DictReader(datei)

            for zeile in reader:
                self.daten.append(zeile)

        return self.daten