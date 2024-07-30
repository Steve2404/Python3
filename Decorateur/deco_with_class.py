from typing import Any


class Verifier():
    def __init__(self, *args) -> None:
        self.function = None
        self.types = args

    def __call__(self, fonction):
        self.function = fonction
        return self.function_verifier

    def function_verifier(self, *args, **kwargs):
        for i in range(len(args)):
            if not isinstance(args[i], self.types[i]):
                return "Invalid type ..."
        return self.function(*args, **kwargs)


# def repeter(chaine, nbre):
#     return chaine * nbre


if __name__ == '__main__':
    # function = Verifier(str, int)
    # funct = function(repeter)
    # sortie = funct("Hello", 3)
    # print(sortie)
    
    # plus facile serait de par un decorateur
    @Verifier(str, int)
    def repeter(chaine, nbre):
        return chaine * nbre
    
    sortie = repeter("Hello", 3)
    print(sortie)
    
