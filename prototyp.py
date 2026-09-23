import csv
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon



#######################################
## Daten auslesen
#######################################

def csv_einlesen(dateiname):
    daten = []
    with open(dateiname, mode="r", encoding="utf-8") as datei:
        reader = csv.DictReader(datei)

        for zeile in reader:
            daten.append(zeile)

    return daten    

daten = csv_einlesen("daten\\Module.csv")



######################################
## ECTS berechnen
######################################

erreichte_ects = 0
noten = []

for zeile in daten:
    if zeile["Bestanden"].strip().lower() == "ja":
        erreichte_ects += float(zeile["ECTS"])

gesamt_ects = 180
rest_ects = max(gesamt_ects - erreichte_ects, 0)



#######################################
## Notendurchschnitt berechnen
#######################################

noten = []

for zeile in daten:
    note = zeile["Note"].strip()

    if note.upper() != "K.A.":
            noten.append(float(note))

if noten:
    notendurchschnitt = sum(noten) / len(noten)
    if notendurchschnitt <= 2.00:
        farbe_achteck="#4CAF50"
    elif notendurchschnitt <= 2.5:
        farbe_achteck="#FFFF33"
    else:
        farbe_achteck="#FF0000"
else:
    notendurchschnitt = 0
    farbe_achteck="#FFFFFF"



#######################################
## Dashboard
#######################################

st.title("Hallo User!")

col1, col2 = st.columns(2)



#######################################
## Linke Sete: Notendurchschnitt
#######################################

with col1:
    fig1, ax1 =plt.subplots(figsize=(5,5))

    achteck = RegularPolygon(
        (0.5, 0.5),
        numVertices=8,
        radius=0.45,
        orientation=22.5 * 3.14159 / 180,
        facecolor=farbe_achteck,
        edgecolor="white",
        linewidth=3
    )

    ax1.add_patch(achteck)

    ax1.text(
        0.5,
        0.55,
        f"{notendurchschnitt:.2f}",
        ha="center",
        va="center",
        fontsize=40,
        fontweight="bold",
        color="black"
    )

    ax1.text(
        0.5,
        0.30,
        "Notendurchschnitt",
        ha="center",
        va="center",
        fontsize=14,
        color="black"
    )

    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis("off")

    st.pyplot(fig1)
    
    if st.button("Noten anzeigen"):
        noten_liste = []

        for zeile in daten:
            noten_liste.append({
                "Modul": zeile["Modul"],
                "Note": zeile["Note"]
            })

        st.dataframe(
            noten_liste,
            use_container_width=True,
            hide_index=True
        )


#######################################
## Rechte Seite: Butten zur Notenansicht
#######################################



#######################################
## Rechte Seite: ECTS-Kreisdiagramm
#######################################

with col2:

    werte = [erreichte_ects, rest_ects]
    labels = ["Erreichte ECTS", "Noch benötigt"]
    farben = ["#008A00", "#FF6666"]

    fig2, ax2 = plt.subplots(figsize=(5, 5))

    ax2.pie(
        werte,
        labels=labels,
        autopct="%1.2f%%",
        startangle=90,
        counterclock=False,
        colors=farben
    )

    ax2.set_title(
        f"ECTS-Fortschritt: {erreichte_ects:g} / {gesamt_ects}"
    )

    st.pyplot(fig2)