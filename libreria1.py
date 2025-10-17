import numpy as np 


vector = np.array([1, 2, 3, 4, 5])
print("Vector:", vector)


suma = np.sum(vector)
media = np.mean(vector)
print("Suma del vector", suma)
print("Media del vector", media)


matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matriz original\n", matriz)

transpuesta = np.transpose(matriz)
print("Matriz transpuesta\n", transpuesta)


multiplicacion = np.dot(matriz, transpuesta)
<<<<<<< HEAD
print("Multiplicación \n", multiplicacion)
#fabian torres
=======
print("Multiplicación \n", multiplicacion)
>>>>>>> a71f0d8445426a98330a9a4d498bd24f46c846db
