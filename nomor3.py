def distribusi_jam(file_):
    distribusi = {}
    with open(file_, 'r') as file:
        for line in file:
            if line.startswith('From '):
                kata = line.split()
                waktu = kata[5].split(':')
                jam = waktu[0]
                distribusi[jam] = distribusi.get(jam, 0) + 1
    
    print("distribusi jam :")
    for jam in sorted(distribusi):
        print(jam, distribusi[jam])
    
file_ = "mbox-short.txt"
distribusi_jam(file_)