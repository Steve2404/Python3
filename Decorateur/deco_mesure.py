import time
from decimal import Decimal

a_mesure = True

def mesure_temps(fonction):
    def wrapper(*args, **kwargs):
        if not a_mesure:
            return fonction(*args, **kwargs)
        debut = time.time()
        print("Temps({} secondes) avant l execution de la fonction".format(debut))
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        diff_time = fin - debut
        print("Temps ({} secondes) apres l execution de la fonction".format(fin))
        print("Temps d'execution de la fonction : {} secondes".format(Decimal(diff_time)))
        return resultat
    return wrapper
    
@mesure_temps
def presentation(nom):
    print(f"Je m appele: {nom}")
    # time.sleep(3)
    
if __name__ == "__main__":
    presentation("Leonel Steve")