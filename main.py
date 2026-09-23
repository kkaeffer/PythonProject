from data_manager import DatenManager
from berechnungen import Berechnungen
from anzeige import Dashboard

# CSV-Datei einlesen und die enthaltenen Daten speichern
data_manager = DatenManager("daten\\Module.csv")
daten = data_manager.daten_einlesen()

# Berechnungen der eingelesenen Daten
berechnung = Berechnungen(daten)

# Dashboard ertstellen und anzeigen
anzeige = Dashboard(berechnung)
anzeige.anzeigen()