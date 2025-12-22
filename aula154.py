class Multiplicar:
    def __init__(self, func):
         self.func = func
    
    def __call__(self, *args, **kwargs):
        print(*args, **kwargs)
        return self.func(*args, **kwargs)
        

@Multiplicar
def soma(x, y):
    return x + y


        

dois_mais_dois = soma(2, 4)

print(dois_mais_dois) 
        