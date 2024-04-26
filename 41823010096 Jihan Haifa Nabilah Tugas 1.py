while (True):
    print ("Selamat Datang di Aplikasi Perhitungan Nilai Mahasiswa")
    tugas = float (input ("Silahkan Masukan Nilai Tugas Anda : "))
    uts = float (input ("Silahkan Masukan Nilai UTS Anda : "))
    uas = float (input ("Silahkan Masukan Nilai UAS Anda : "))

    nilai = (0.25 * tugas + 0.35 * uts + 0.40 * uas)

    print ("Nilai Akhir Anda", nilai)

    if nilai > 85 :
        print ("Dalam Huruf : A")
    elif nilai > 80 :
        print ("Dalam Huruf A-")
    elif nilai > 75 :
        print ("Dalam Huruf : B+")
    elif nilai > 70  :
        print ("Dalam Huruf B")
    elif nilai > 65 :
        print ("Dalam Huruf B-")
    elif nilai > 60 :
        print ("Dalam Huruf C+")
    elif nilai > 55 :
        print ("Dalam Huruf C")
    elif nilai > 60 :
        print ("Dalam Huruf C-")
    elif nilai > 30 :
        print ("Dalam Huruf D")
    else :
        print ("Dalam Huruf E")