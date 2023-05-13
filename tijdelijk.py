prijzen={
    "aardbei":3,
    "vanille":4,
    "chocoldade":5
}
import decimal
aanbieding=round(decimal.Decimal(prijzen["aardbei"]*0.8),2)
reclame_tekst=(f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
reclame_tekst3=reclame_tekst.upper()
reclame_tekst4=reclame_tekst3.split()
# for el in reclame_tekst4:
#    print(el.lower())
for el in reclame_tekst4:
    if len(el)<5:
          print(el.lower())
    else:
       print(el)
