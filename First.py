def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        return "Číslo {} je sudé".format(cislo)
    else:
        return "Číslo {} je liché".format(cislo)

print(sudy_nebo_lichy(5))
print(sudy_nebo_lichy(1000000))
