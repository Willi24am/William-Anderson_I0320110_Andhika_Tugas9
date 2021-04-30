import array
# Exercise 9.9
A = array.array('i', [100,200,300,400,500])
print(A)

A[1] = -700
A[4] = 800
print(A)

# nilai awal (sebelum dibalik)
print(A)

# membalik urutan elemen array
A.reverse()

# nilai akhir (setelah dibalik)
print(A)