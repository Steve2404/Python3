def mon_decorateur_avec_parametre(prefix):
    def decorateur_reel(fonction):
        def fonction_decoree(*args, **kwargs):
            print(f"{prefix} Appel de la fonction {fonction.__name__} ...")
            print(f"Les arguments sont: {args} {kwargs}")
            result = fonction(*args, **kwargs)
            print(f"{prefix} Fin de l'appel de la fonction {fonction.__name__}")
            return result
        return fonction_decoree
    return decorateur_reel

@mon_decorateur_avec_parametre(">>>")
def gretting(nom):
    return f"Bonjour {nom}"

if __name__ == "__main__":
    print(gretting("leonel"))
    print(gretting("steve"))