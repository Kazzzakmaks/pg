def je_prvocislo(cislo):
    
    if cislo <= 1:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    
    return [cislo for cislo in range(2, maximum + 1) if je_prvocislo(cislo)]

if __name__ == "__main__":
    try:
        maximum = int(input("Zadej maximum: "))
        prvocisla = vrat_prvocisla(maximum)
        print(prvocisla)
    except ValueError:
        print("Zadej platné celé číslo!")
