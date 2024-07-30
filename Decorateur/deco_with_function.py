def mon_decorateur(func):
    def func_decore(*args, **kwargs):
        print(func.__name__, " est appelee")
        print("Les arguments sont: {}".format(args))
        return func(*args, **kwargs)
    return func_decore


@mon_decorateur
def presentation(nom):
    print(f"Je m appelle: {nom}")

if __name__ == "__main__":
    presentation("Leonel")