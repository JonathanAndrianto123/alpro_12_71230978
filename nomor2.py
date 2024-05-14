def data_diri(nim, nama, alamat) :
    data = nama, nim, alamat
    print(data)
    print()
    print(f"NIM     : {nim}")
    print(f"Nama    : {nama}")
    print(f"Alamat  : {alamat}")
    print()
    print(f"Nim : {tuple(nim)}")
    print(f"Nama Depan : {tuple(nama.split()[0])}")
    print(f"Nama Terbalik : {tuple(nama.split()[::-1])}")


nim = "22064091"
nama = "Matahari Bhakti Nendya"
alamat = "Bantul, DI Yogyakarta"
data_diri(nim, nama, alamat)