A = set({'a', 'b', 'c', 'd'})
B = set({'c', 'd', 'e'})
C = set({})

print(A ^ B)
print(B ^ A)
print(A ^ C)
print(C ^ A)

# Output
# {'b', 'e', 'a'}
# {'a', 'b', 'e'}
# {'c', 'b', 'd', 'a'}
# {'b', 'd', 'c', 'a'}