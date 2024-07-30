def fonction():
    data = yield "Hello word"
    print(f"Donnee recue: {data}")
    
func = fonction()
print(list(func))
for string in func:
    print(string)
    # func.send("Bonjour")
# func.__next__()#
if __name__ == "__main__":
    liste = [2, 3, 4, 5, 6]
    chaine = "Hello world"
    print(list(liste.__iter__()))
    print(list(chaine.__iter__()))
    print(list(range(5)))
