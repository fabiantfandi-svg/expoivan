import dask.array as da


x = da.random.randint(1, 11, size=10, chunks=5)


print("Números generados:")
print(x.compute())


media = x.mean()


print("Promedio:")
<<<<<<< HEAD
print(media.compute())
#fabian torres
=======
print(media.compute())
>>>>>>> a71f0d8445426a98330a9a4d498bd24f46c846db
