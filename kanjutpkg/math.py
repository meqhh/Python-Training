"""
Matematika basic doang ygy, maaf masih pemula
"""
def penjumlahan(*args):
    """
    Penjumlahan dengan argumen parameter yang bisa lebih dari 2.
    jadi tolong isi parameternya harus integer atau float ya

    math.penjumlahan(arg1, arg2, dst)
    """
    if not args:
        return 'Parameternya tolong di isi dek'

    for i in args:
        if isinstance(i, str):
            return 'Harus Float atau Integer ya dek'

    if len(args) == 1:
        return 'Argumen parameter harus lebih 1 dari dek kalau cuman 1 mau nambah apaan lu kocak'

    result = 0

    for i in args:
        result += i

    return result

def pengurangan(*args):
    """
    Pengurangan dengan argumen parameter yang bisa lebih dari 2.
    jadi tolong isi parameternya harus integer atau float ya


    math.pengurangan(arg1, arg2, dst)
    """
    if not args:
        return 'Parameternya tolong di isi dek'

    for i in args:
        if isinstance(i, str):
            return 'Harus Float atau Integer ya dek'

    if len(args) == 1:
        return 'Argumen parameter harus lebih 1 dari dek kalau cuman 1 mau ngurangin apaan lu kocak'

    result = args[0]

    for i in args[1:]:
        result -= i

    return result

def perkalian(*args):
    """
    perkalian dengan argumen parameter yang bisa lebih dari 2.
    jadi tolong isi parameternya harus integer atau float ya


    math.perkalian(arg1, arg2, dst)
    """
    if not args:
        return 'Parameternya tolong di isi dek'

    for i in args:
        if isinstance(i, str):
            return 'Harus Float atau Integer ya dek'

    if len(args) == 1:
        return 'Argumen parameter harus lebih 1 dari dek kalau cuman 1 mau kali apaan lu kocak'

    result = 1

    for i in args:
        result *= i

    return result

def pembagian(*args):
    """
    pembagian dengan argumen parameter yang bisa lebih dari 2.
    jadi tolong isi parameternya harus integer atau float ya

    contoh penggunaan
    math.perkalian(arg1, arg2, dst)
    """
    if not args:
        return 'Parameternya tolong di isi dek'

    for i in args:
        if isinstance(i, str):
            return 'Harus Float atau Integer ya dek'

    if len(args) == 1:
        return 'Argumen parameter harus lebih 1 dari dek kalau cuman 1 mau bagi apaan lu kocak'

    result = args[0]

    for i in args[1:]:
        if i == 0:
            return 0
        else:
            result /= i

    return result

def ganjilgenap(*args):
    """
    ganjil genap dengan argumen parameter yang bisa lebih dari 2.
    jadi tolong isi parameternya harus integer atau float ya

    contoh penggunaan
    math.ganjilGenap(arg1, arg2, dst)
    """
    if not args:
        return 'Parameternya tolong di isi dek'

    for i in args:
        if isinstance(i, str):
            return 'Harus Float atau Integer ya dek'

    hasil = []
    for i in args:
        if i % 2 == 0:
            hasil.append(f'{i} adalah Genap')
        else:
            hasil.append(f'{i} adalah Ganjil')

    for j in hasil:
        print(j)

def pangkat(*args):
    """
    Perpangkatan dalam matematika, function ini hanya menerima 2 parameter saja
    kalau lebih atau kurang dari 2 tidak akan bekerja, dan tipe yang dapat diterima hanyalah
    float atau integer

    contoh penggunaan
    math.pangkat(arg1, arg2)
    """
    if not args:
        return 'Parameternya tolong di isi dek'

    for i in args:
        if isinstance(i, str):
            return 'Harus Float atau Integer ya dek'

    if len(args) == 2:
        panjang = args[1]
        hasil = 1

        for i in range(panjang):
            hasil *= args[0]
        return hasil
    else:
        return 'Argumen harus 2 ga boleh lebih atau kurang ya dek'