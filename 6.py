A = set({'a', 'b', 'c', 'd'})
B = set({'c', 'd', 'e'})
C = set({})

print(A - B)
print(B - A)
print(A - C)
print(B - C)

# Output
# {'a', 'b'}
# {'e'}
# {'c', 'd', 'a', 'b'}
# {e, c, d}