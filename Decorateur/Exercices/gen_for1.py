def queue(*args):
    elems = list(args)
    while elems:
        new = yield elems.pop(0)
        if new is not None:
            elems.append(new)


q = queue('a', 'b', 'c')
for letter in q:
    if letter == 'a':
        q.send('d')
    print(letter)
    
"""
Ici on remarque que  la boucle for a chaque iteration appelle de maniere 
implecite next(), et quand la condition est satisfaite on fait un q.send('d')
qui a pour effet d initialiser la variable new et de d ajouter 'd' a la liste
mais sauf qu il continue l operation jusqu au prochain yield, ce qui a pour 
effect de retirere 'b' de la liste et de renvoye ca gra ce a yield, mais 
au retour dans la boucle on continue ou on s etait arrete juste apres le 
send, donc le print(), et c est 'a' qui est affiche.
La boucle fait appel a nouveau a next(), mais vu que 'b' a ete retire ce qui
reste c est 'c' et 'd' 

"""