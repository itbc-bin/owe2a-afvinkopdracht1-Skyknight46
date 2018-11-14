# Naam: Tom Ummenthun
# Datum: 14-11-'18
# Versie: 1

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

import easygui

def main():
    """Main functie die structuur in script bewaard"""
    bestand = easygui.fileopenbox(title=None, default="*", filetypes=["*.fna"])
    headers, seqs = lees_inhoud(bestand)
    totalhitcounter = 0
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:", headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
                totalhitcounter += 1
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")

            if totalhitcounter == 0:
                print("zoekwoord komt niet voor in headers")
                main()


def lees_inhoud(bestands_naam):
    """Inlezen van bestand en headers er uit halen.
    input is string met bestandsnaam
    """
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
                headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs


def is_dna(seq):
    """Controleren of input sequentie DNA is door tellen van A, T, G, C en vergelijken met totale lengte sequentie
    INPUT: is sequentie op dezelfde posities in de lijst als het zoekwoord in headers lijst
    OUTPUT: returned boolean True wanneer de aangeleverde sequentie DNA was, False wanneer dit niet het geval was
    """
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    """controleren of de restrictie enzymen knippen in de sequenties behorend tot je zoekwoord
    input is sequentie uit seq lijst op dezelfde locatie als de bijbehorende match met het zoekwoord in headers lijst
    """
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq=line.split(" ")
        seq = seq.strip().replace("^", "")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")


main()
