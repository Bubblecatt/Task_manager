# Seznam pro ukládání úkolů
ukoly = []

# Funkce pro hlavní menu
def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní Menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Zadejte volbu (1-4): ")
        
        if volba == '1':
            pridat_ukol()
        elif volba == '2':
            zobrazit_ukoly()
        elif volba == '3':
            odstranit_ukol()
        elif volba == '4':
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

# Funkce pro přidání úkolu
def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        if not nazev:
            print("Název úkolu nesmí být prázdný!")
            continue
        
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný!")
            continue
        
        ukoly.append({'nazev': nazev, 'popis': popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

# Funkce pro zobrazení všech úkolů
def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly nejsou k dispozici.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. Úkol - {ukol['popis']}")

# Funkce pro odstranění úkolu
def odstranit_ukol():
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return
    
    zobrazit_ukoly()
    
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        if cislo < 1 or cislo > len(ukoly):
            print("Neexistující úkol. Zkuste to znovu.")
        else:
            odstraneny_ukol = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.")
    except ValueError:
        print("Neplatné číslo úkolu.")

# Spuštění programu
hlavni_menu()
