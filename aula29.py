frase = 'olha interessante'
lista_palavra = frase.split()
print(lista_palavra)
list_frase = []
for i, frase in enumerate(lista_palavra):
    list_frase.append(lista_palavra[i].strip())

frases_unidas = '.'.join(list_frase)
print(frases_unidas)