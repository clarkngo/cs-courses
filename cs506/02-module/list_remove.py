#del
motercycles = ['honda','yamaha', 'suzuki']
del motercycles[1]
print(motercycles)

#pop
motercycles = ['honda','yamaha', 'suzuki']
popped_motercycles = motercycles.pop()
print(motercycles)
print(popped_motercycles)
first_owned=motercycles.pop(0)
print("the first motorcycle I owned was a", first_owned)

#remove
motercycles= ['honda','yamaha', 'suzuki','ducati']
motercycles.remove('ducati')
print(motercycles)

