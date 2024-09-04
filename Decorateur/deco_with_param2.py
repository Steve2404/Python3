from functools import wraps
def decorateur(guess_name):
    def wrapper1(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Je vais devinez votre nom !!!")
            valeur = func(*args, **kwargs)
            nom = args[0]
            if nom != guess_name:
                print(valeur)
            else:
                print(f"J ai devine votre nom, {guess_name.upper()} 😁")
            print("fin de la presentation !!!")
        return wrapper
    return wrapper1

@decorateur("Jatsa")
def presentation(nom, prenom):
    """fonction de presentation

    Args:
        nom (_type_): le nom sous forme de str
        prenom (_type_): prenom sous forme de str

    Returns:
        _type_: str
    """

    return f"je m appelle {prenom} {nom}"

presentation("Jatsa", "Leonel Steve")

"""
on peut executer de cette maniere sans passer par un sucre syntaxtique 

decorateur(presentation("Jatsa", "Leonel Steve"))

"""
