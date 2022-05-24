# Database menggunakan dictionary di dalam list
Database=[
    {'ID':'YP1','first_name':'Ayi','last_name':'sayi','lokasi':'Jakarta','nomor':'087801300100'},
    {'ID':'YP2','first_name':'Emyr','last_name':'lemyr','lokasi':'Bandung','nomor':'78893680'},
    {'ID':'YP3','first_name':'Andri','last_name':'randri','lokasi':'Bogor','nomor':'78883733'},
    ]

# Function untuk show all in database
def showdatabase():
    if Database==[]: #apabila tidak ada data, akan print 'tidak ada data'
        print('\nTidak ada data!')
    else :
        for i in range(len(Database)):
                print(f'{i+1}. ID :{Database[i]["ID"]}, first name :{Database[i]["first_name"]}, last name :{Database[i]["last_name"]}, lokasi :{Database[i]["lokasi"]}, nomor :{Database[i]["nomor"]}')
    
# Function untuk find ID in database 
def Find(ID):
    global findcheck
    findcheck=False  
    for i in range(len(Database)):
        if Database[i]['ID']==ID:
            findcheck=True         
            break
        else:
            findcheck=False

# Function untuk find kolom in database 
def Findkolom(kolom):
    global Kolomfound
    Kolomfound = False 
    if kolom == 'first_name' or kolom == 'lokasi' or kolom == 'last_name' or kolom == 'nomor':
        Kolomfound = True

# Function untuk query 1 ID (return value dari ID)
def query(ID):
    global index_found    # index_found akan digunakan untuk indexing di menu merubah & menghapus data
    for i in range(len(Database)):
        if Database[i]['ID']==ID:
            index_found=i                # keep index untuk fungsi selanjutnya
            print(f'{1}. ID :{Database[i]["ID"]}, first name :{Database[i]["first_name"]}, last name :{Database[i]["last_name"]}, lokasi :{Database[i]["lokasi"]}, nomor :{Database[i]["nomor"]}')

#Function untuk menjalankan applikasi yang mencakup semua fungsi menu
def menu():
    while True :
        print('''
                                                                                          
         __ __ _____ __    __    _____ _ _ _    _____ _____ _____ _____ _____         
 ___ ___|  |  |   __|  |  |  |  |     | | | |  |  _  |  _  |   __|   __|   __|___ ___ 
|___|___|_   _|   __|  |__|  |__|  |  | | | |  |   __|     |  |  |   __|__   |___|___|
          |_| |_____|_____|_____|_____|_____|  |__|  |__|__|_____|_____|_____|        
                                                                                      
    Selamat datang Yellow Pages!

    List menu : 
    1. Menampilkan Data Nomor Telfon
    2. Menambah Data Nomor Telfon
    3. Mengubah Data Nomor Telfon
    4. Menghapus Data Nomor Telfon
    5. Exit program
        ''')
        choose=input('Masukkan angka menu yang ingin di jalankan [1-5]: ')
        if choose=='1':
            menu_1()
        elif choose=='2':
            menu_2()
        elif choose=='3':
            menu_3()
        elif choose=='4':
            menu_4()
        elif choose=='5':
            print('Applikasi akan tertutup, Terima kasih')
            break
        else:
            print('\nPilihan yang anda masukkan salah!')

# Function yang mendvjalankan fungsi menampilkan data
def menu_1():
    while(True):
        print('''
        =====Menampilkan Data Nomor Telfon=====
        1. Tampilkan semua Nomor telfon
        2. Tampilkan sebuah Nomor telfon
        3. Balik ke Main Menu
         ''')
        choose=input('Masukkan angka menu yang ingin di jalankan [1-3]: ')
        if choose=='1':
            showdatabase()
        elif choose=='2':
            while(True):
                Pilih=input('masukkan ID yang ingin dilihat : ')
                Find(Pilih)                 # Mencari ID
                if findcheck == True:
                    query(Pilih)            # show value berdasarkan ID
                    break
                else :
                    print('\nData tidak ada')
                    break
        elif choose=='3':
            break
        else:
            print('Pilihan yang anda masukkan salah!')

# Function yang menjalankan fungsi menambah data
def menu_2():
    while(True):
        print('''
        =====Menambah Data Nomor Telfon=====
        1. Tambah data Nomor telfon
        2. Balik ke Main Menu
         ''')
        choose=input('Masukkan angka menu yang ingin di jalankan [1-2]: ')
        if choose=='1':
            input_id=input('masukkan ID yang ingin diinput : ')
            Find(input_id)                  # Mencari ID
            if findcheck == True:
                    print('\nData dengan ID tersebut sudah ada')
            else :
                input_fnama=input('masukkan nama depan pemilik nomor : ')
                input_lnama=input('masukkan nama belakang pemilik nomor : ')
                input_lokasi=input('masukkan lokasi pemilik nomor : ')
                input_nomor=input('masukkan nomor telfon : ')
                while(True):                    # untuk confirm penambahan data
                    confirm=input('apakah data ingin diupdate? [Y/N]')
                    if confirm == 'Y':
                        Database.append({'ID':input_id,'first_name':input_fnama,'last_name':input_lnama,'lokasi':input_lokasi,'nomor':input_nomor})
                        print('\nDatabase berhasil ditambah!')
                        break
                    elif confirm == 'N':
                        break
                    else:
                        print('\ninput yang anda masukkan salah\n')
        elif choose=='2':
            break
        else :
             print('\ninput yang anda masukkan salah')

# Function yang menjalankan fungsi mengubah data
def menu_3():
    while(True):
        print('''
        =====Mengubah Data Nomor Telfon=====
        1. Ubah data Nomor telfon
        2. Balik ke Main Menu
        ''')
        choose=input('Masukkan angka menu yang ingin di jalankan [1-2]: ')
        if choose=='1':
            input_id=input('masukkan ID yang ingin diinput : ')
            Find(input_id)                      # Mencari ID
            if findcheck != True:
                print("\nData yang anda cari tidak ada!")
            else :
                while(True):
                    query(input_id)             # show value berdasarkan ID
                    choose=input('apakah data ingin diubah? : [Y/N] ')
                    if choose == 'Y':
                        kolomchange=input('Input kolom yang ingin diubah : [first_name/last_name/lokasi/nomor]')
                        Findkolom(kolomchange)  # find kolom in database
                        if Kolomfound == True:
                            Value=input('Masukkan value yang diinginnkan :')
                            while(True):                 # untuk confirm perubahan data
                                confirm=input('apakah data ingin diupdate? [Y/N]')
                                if confirm == 'Y':
                                    Database[index_found][kolomchange]=Value  # index_found dari fungsi query(ID)
                                    print('\nData berhasil terupdate!')
                                    break
                                elif confirm == 'N':
                                    break
                                else:
                                    print('\ninput yang anda masukkan salah \n')
                        else :
                            print('\nKolom tidak ditemukan')
                        break
                    elif choose == 'N':
                        break
                    else:
                        print('\ninput yang anda masukkan salah \n')
        elif choose =='2':
            break
        else :
            print('\ninput yang anda masukkan salah ')

# Function yang menjalankan fungsi menghapus data
def menu_4():
    while(True):
        print('''
        =====Menghapus Data Nomor Telfon=====
        1. Hapus data Nomor telfon
        2. Balik ke Main Menu
        ''')
        choose=input('Masukkan angka menu yang ingin di jalankan [1-2]: ')
        if choose=='1':
            input_id=input('masukkan ID yang ingin diinput : ')
            Find(input_id)
            if findcheck != True:
                print("\nData yang anda cari tidak ada!")
            else :
                while(True):
                    query(input_id)
                    choose=input('apakah data ingin dihapus? : [Y/N] ')
                    if choose == 'Y':
                        Database.pop(index_found)       #index_found dari fungsi query(ID)
                        print('\nData berhasil dihapus!')
                        break
                    elif choose == 'N':
                        break
                    else :
                        print('\ninput yang anda masukkan salah')
        elif choose=='2':
            break
        else:
            print('\ninput yang anda masukkan salah')

menu()

    