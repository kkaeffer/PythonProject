import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon#

# Klasse Dashbaord für die Darstellung
class Dashboard:

    def __init__(self, berechnungen):
        self.berechnungen = berechnungen

    # grundlegende Ansicht des Dashboards in zwei Spalten aufgeteilt
    def anzeigen(self):
        st.title("Hallo User!")

        col1, col2 = st.columns(2)

        with col1:
            self.notendurchschnitt()

        with col2:
            self.fortschritt()

    # Notendurchschnittanzeige 
    def notendurchschnitt(self):
        notendurchschnitt = self.berechnungen.notendurchschnitt_berechnen()
        farbe = self.berechnungen.farbe_achteck_berechnen()

        fig, ax = plt.subplots(figsize=(5, 5))

        # Achteckdesign, farbe wird in berechnung.py festgelegt
        achteck = RegularPolygon(
            (0.5, 0.5),
            numVertices=8,
            radius=0.45,
            orientation=22.5 * 3.14159 / 180,
            facecolor=farbe,
            edgecolor="white",
            linewidth=3
        )

        # Achteck anzeigen
        ax.add_patch(achteck)

        # Achteckbeschriftung Zahl
        ax.text(
            0.5,
            0.55,
            f"{notendurchschnitt:.2f}",
            ha="center",
            va="center",
            fontsize=40,
            fontweight="bold",
            color="black"
        )

        #Achteckbeschriftung Beschreibung
        ax.text(
            0.5,
            0.30,
            "Notendurchschnitt",
            ha="center",
            va="center",
            fontsize=14,
            color="black"
        )

        # Setzen der Achteckposition und blendet die Achse aus
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        st.pyplot(fig)

        # Zeigt bei Klick auf Button die einzlenen Modulnoten an
        if st.button("Noten anzeigen"):
            self.noten_anzeigen()

    # Erstellt Tabelle mit den Modulnoten
    def noten_anzeigen(self):
        noten_liste = self.berechnungen.noten_liste_erstellen()

        st.dataframe(
            noten_liste,
            use_container_width=True,
            hide_index=True
        )

    # Kreisdiagramm des ECTS-Fortschritt
    def fortschritt(self):
        erreichte_ects = self.berechnungen.erreichte_ects_berechnen()
        rest_ects = self.berechnungen.rest_ects_berechnen()
        gesamt_ects = self.berechnungen.gesamt_ects

        werte = [erreichte_ects, rest_ects]

        labels = [
            "Erreichte ECTS",
            "Noch benötigt"
        ]

        farben = [
            "#008A00",
            "#FF6666"
        ]

        # Kreisdiagramm erstellen
        fig, ax = plt.subplots(figsize=(5, 5))

        # Kreisdiagrammdesign
        ax.pie(
            werte,
            labels=labels,
            autopct="%1.2f%%",
            startangle=90,
            counterclock=False,
            colors=farben
        )

        # Überschrift Kreisdiagramm
        ax.set_title(
            f"ECTS-Fortschritt: {erreichte_ects:g} / {gesamt_ects}"
        )

        # Kreisdiagramm anzeigen
        st.pyplot(fig)