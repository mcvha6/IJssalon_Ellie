from helper import som

def presenteer(mijn_dict):
    
    totaal=som(mijn_dict)
    
    print()
    for k,v in mijn_dict.items():
        print(f"{k} : {v} euro.")
        
    print("=========================")
    print(f"totaal = {totaal} euro.")
    print()

