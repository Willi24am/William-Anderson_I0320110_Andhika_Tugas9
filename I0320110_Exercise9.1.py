import sys

# Mendefinisikan array konstan
hari = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')

def main():
    # Meminta user memasukkan nomor hari
    nohari = int(input("Masukkan nomor hari [1...7]: "))

    if (nohari<1) or (nohari>7):
        print("Tidak ada hari ke-%s" % nohari)
        sys.exit()

    print(("Hari ke-%d adalah %s" %(nohari, hari[nohari-1])))

if __name__ == "__main__":
    main()