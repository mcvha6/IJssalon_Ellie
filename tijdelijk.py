from helper import decoreer

def print_aanbieding():
    prijzen={
        "aardbei":3,
        "vanille":4,
        "chocoldade":5
    }
    import decimal
    aanbieding=round(decimal.Decimal(prijzen["aardbei"]*0.8),2)
    reclame_tekst=(f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
    reclame_tekst4=reclame_tekst.split()
    for el in reclame_tekst4:
        if len(el)<5:
            print(el.lower())
        else:
            print(el.upper())
decoreer("Aanbieding")
print_aanbieding()