import random
# diccionario = dict ()



# peli1 = 'Volver al Futuro'
# peli2 = 'Jurassic World'
# peli3 = 'Avatar'
# diccionario[peli1] = "Michael Fox"
# diccionario[peli2] = "Juan Perez"
# diccionario[peli3] = "Micaela Ramos"

# for n_pelicula in diccionario:
#     print (n_pelicula, "," + diccionario[n_pelicula])


# inicializa diccionario
# p_n = dict ()
# p_n['par'] = 0
# p_n['impar'] = 0

# for i in range (100):
#     n_a = random.randint (1, 100)
#     # print (i, n_a)
#     if n_a % 2 == 0:
#         # contar pares
#         p_n['par'] = p_n['par'] + 1
#     else:
#         # contar impares
#         p_n['impar'] += 1

# print (p_n)


p_n = dict ()
p_n['par'] = []
p_n['impar'] = []

for i in range (10):
    n_a = random.randint (1, 100)
    # print (i, n_a)
    if n_a % 2 == 0:
        # contar pares
        p_n['par'].append (n_a)
    else:
        # contar impares
        p_n['impar'].append (n_a)


# sobre las llaves
for elem in p_n.items ():
    print (elem)
