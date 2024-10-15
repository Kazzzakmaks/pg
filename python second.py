def cislo_text(cislo):
    # Převod vstupního čísla na celé číslo
    cislo = int(cislo)
    
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky_do_20  = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if 0 <= cislo < 10:
        return jednotky[cislo]
    elif 10 < cislo < 20:
        return desitky_do_20 [cislo - 11]
    elif cislo == 10:
        return desitky[1]
    elif 20 <= cislo < 100:
        deset = desitky[cislo // 10]
        jednotka = jednotky[cislo % 10]
        return deset if jednotka == "nula" else f"{deset} {jednotka}"
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)

