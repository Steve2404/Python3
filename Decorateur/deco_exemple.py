def mon_decorateur(function):
    print("Initialisation du decorateur ....")
    counter = 0
    def ma_fonction_decore(*args, **kwargs):
        nonlocal counter 
        counter += 1
        print("Appel de la fonction {} ...".format(function.__name__))
        print("Les Arguments sont: {}".format(args))
        print("Nombre d'appels: {}".format(counter))
        if args and isinstance(args[0], str) and args[0].isalpha():
            args = (args[0].capitalize(),) + args[1:]
        return function(*args, **kwargs)
    return ma_fonction_decore

@mon_decorateur
def gretting(nom):
    return f"Bonjour {nom}"

if __name__ == "__main__":
    print(gretting("leonel"))
    print(gretting("steve"))
        