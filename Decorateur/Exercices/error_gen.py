def generator():
    valeur = yield "premier yield"
    print(f"Valeur recue: {valeur}")
    valeur = yield "deuxieme yield"
    print(f"Valeur recue: {valeur}")
    yield "fin du generator"
    

if __name__ == "__main__":
    gen = generator()
    print(gen.send(None))
    print(gen.send("nouvelle valeur"))
    print(next(gen))
    