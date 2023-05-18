from algemene_functies import mijn_functie_2
import decimal

def aanbieding_1(smaak="",prijs=3,korting=0.1):

    import decimal
    
    print()
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor",round(decimal.Decimal(prijs-prijs*korting),2),"euro.")
    print()

def inkomsten_totaal(inkomsten):

    import decimal

    btw=0.09    

    totaal=0
    for som in inkomsten:
        totaal+=+som

    print()
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover",round(decimal.Decimal(totaal/(1+btw)*btw),2),"euro btw betaald dient te worden.")
    print()

def laag_en_hoog(mijn_lijst):

    max_lh=max(mijn_lijst)
    min_lh=min(mijn_lijst)

    uitvoer=([min_lh,max_lh])
    return uitvoer

def gemiddelde(mijn_lijst):
    
    totaal=0
    a=0
    for som in mijn_lijst:
        totaal+=+som
        a+=+1

    uitvoer=totaal/a
    
    return uitvoer

def meervoudig(invoer_lijst=[10,5,3,2,1,2,9]):
    
    global max_meervoudig,min_meervoudig

    if len(invoer_lijst)<5:
        print()
        print("Moet minimaal 5 of maximaal 10 waardes hebben")
        print()

    else:
        if len(invoer_lijst)>10:
            print()
            print("Moet minimaal 5 of maximaal 10 waardes hebben")
            print()

        else:
            
            uitvoer=laag_en_hoog(invoer_lijst)
    
    return uitvoer
    
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

smaak="aardbei"
prijs=4
korting=0.1
    
inkomsten=[220, 430, 125, 160, 205, 90, 345]
invoer_lijst=[10,5,3,2,1,2,9]

# start

aanbieding_1(smaak,prijs,korting)

inkomsten_totaal(inkomsten)

print()
print(f"De hoogste omzet bedraagt {laag_en_hoog(inkomsten)[1]} euro.")
print(f"Je laagste omzet bedraagt {laag_en_hoog(inkomsten)[0]} euro.")
print()
print("De gemiddelde inkomsten deze week zijn",round(decimal.Decimal(gemiddelde(inkomsten)),2),"euro.")
print()
print(f"Het hoogste getal is",meervoudig(invoer_lijst)[1])
print(f"Het laagste getal is",meervoudig(invoer_lijst)[0])
print()
print(combinatie(invoer_lijst))
