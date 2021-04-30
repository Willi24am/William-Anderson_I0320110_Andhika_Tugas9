import array

# Mengonversi string ke dalam array.array
B = array.array('b')
B.fromstring ("Python")

for karakter in B:
    print("%b " % karakter, end='')