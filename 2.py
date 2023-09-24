nilai = {3, 6, 9, 2, 5, 7}
nilai.update({1, 4, 8})

print(nilai)

nilai.remove(1)
nilai.remove(3)
nilai.remove(4)
nilai.remove(5)
nilai.remove(7)
nilai.remove(8)

nilai1 = list(nilai)

print(nilai)

# Output
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# {2, 6, 9}