def queue(*args):
    elems = list(args)
    while elems:
        new = yield elems.pop(0)
        while new is not None:
            elems.append(new)
            new = yield
            
if __name__ == '__main__':
    q = queue('a', 'b', 'c')
    for letter in q:
        if letter == 'a':
            q.send('d')
        print(letter)
    
    
"""
ceci est la correction du programme gen_for1.py
"""