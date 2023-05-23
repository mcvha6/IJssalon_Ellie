def decoreer(tekst=""):

    lengte=len(tekst)+4
    print()
    print(lengte*"*")
    print(f"* {tekst} *")
    print(lengte*"*")
    print()

def fooi_pp(bedrag,personen):

    bedrag_pp=bedrag/personen
    bedrag_pp="??"
    return f"Het bedrag dat ieder krijgt bedraagt, {bedrag_pp} euro"

def onderstreep(tekst=""):

    uit=[]
    uit.append(tekst)
    uit.append(len(tekst)*"=")
    return uit

def som(dictor):
    try:
        tot=0
        for el in dictor.values():
            tot+=el
        return tot
    except:
        print("Fout in dictionary")
        tot=0
        return tot

