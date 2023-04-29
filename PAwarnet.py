from prettytable import PrettyTable
#class untuk menampung data
class Node:
    def __init__(self, data,jam=0,harga=0):
        self.data = data
        self.jam = jam
        self.harga = harga
        self.next = None

#class yang akan digunakan oleh admin
class LinkedList:
    def __init__(self):
        self.head = None

    #tambah data
    def tambahbilling(self, data,jam,harga):
        if self.head is None:
            self.head = Node(data,jam,harga)
        else: 
            nodebaru = Node(data,jam,harga)
            nodebaru.next = self.head
            self.head = nodebaru

    #hapus data
    def hapusbilling(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print()
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next

    #cari data
    def search(self, nama):
        current = self.head
        ketemu=0
        index=0
        while current is not None:
            if nama == current.data:
                b = databilling.urutan(index)
                hapusdatawarnet.tambahbilling(b.data,b.jam,b.harga)   
                databilling.hapusbilling(index)
                user.append(b.data,b.jam,b.harga)
                return 
            current = current.next
            index += 1
        print (0)
    def searchs(self, nama):
        current = self.head
        ketemu=0
        index=0
        while current is not None:
            if nama == current.data:
                b = databilling.urutan(index)
                print("Billing dengan nama", b.data,"durasi",b.jam,"dan harga",b.harga)
                return 
            current = current.next
            index += 1
        print (0)

def searchss(self, nama):
        current = self.head
        ketemu=0
        index=0
        while current is not None:
            if nama == current.data:
                return 1
            current = current.next
            index += 1
        return 0

    #cari data sesuai index
    def shellShort(self, data):
        try:
            gap = (len(data)//2)
            a=0
            while gap > 0 :
                for i in range(gap,len(data)):
                    value = data[i]
                    j = i
                    while j >= gap and data[j-gap] > value:
                        data[j] = data[j-gap]
                        j-=gap
                    data[j] = value
                    print(data)
                print("Iterasi ke",a,": ",data,"dengan gap ",gap )
                a+=1
                gap //= 2
        except:
            pass

def jumpSearch(self,arr, x):
        if self.head is None :
            self.head = Node(arr)
            self.head = Node(x)
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n) - 1] < x:
            prev = step
            step += int(n ** 0.5)
            if prev >=n:
                return -1
        while arr[prev] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev] == x:
            return prev
        return -1
    def urutan(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1

    #tampilkan semua data
    def tampildatabilling(self):
        if self.head is None:
            print("Tidak ada billing")
            return -1
        else :
            tabelbilling = PrettyTable()
            tabelbilling.field_names = ["No", "Nama Billing",  "Jam", "Harga"]
            n = self.head
            a = 1
            while n is not None:
                tabelbilling.add_row([a, n.data, n.jam,n.harga])
                a += 1
                n = n.next
            print(tabelbilling)

#class yang nanti akan digunakan oleh user
class User:
    def __init__(self):
        self.head = None

    #fungsi yang digunakan untuk menambahkan data
    def append(self, data,jam,harga):
        new_node = Node(data,jam,harga)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    #fungsi untuk menghapus data
    def hapusbilling(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print()
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next1

    #mencari data sesuai index
    def urutan(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1

    #menampilkan semua data
    def print_list(self):
        if self.head is None:
            print("Tidak ada data")
            return -1
        else :
            tabeldata = PrettyTable()
            tabeldata.field_names = ["No", "Nama Billing", "Jam", "Harga"]
            n = self.head
            a = 1
            while n is not None:
                tabeldata.add_row([a, n.data, n.jam, n.harga])
                a += 1
                n = n.next
            print(tabeldata.get_string(sortby="Nama Billing")) 

#inisialisasi variable
user = User()
databilling = LinkedList()
tambahdatawarnet = LinkedList()
hapusdatawarnet = LinkedList()

#fungsi untuk menambahkan billing
def menambahdatabilling():
    inputA = ""
    while inputA == "":
        inputA = input("Masukkan nama billing baru : ")
        if inputA == "":
            print("Masukan inputan dengan benar")
        if databilling.searchss(inputA) == 1:
            print("Nama Sudah Dipakai")
            inputA=""
    b=0
    c=0
    while True:
        try:
            b = int(input("Masukkan Durasi billing baru(jam) : "))
            break
        except:
            print("Masukan Data Berupa Angka")
    while True:
        try:
            c = int(input("Masukkan Harga billing baru : "))
            break
        except:
            print("Masukan Data Berupa Angka")
    databilling.tambahbilling(inputA,b,c)
    tambahdatawarnet.tambahbilling(inputA,b,c)

#fungsi untuk menghapus data billing
def menghapusdatabilling():
    try:
        hapus =""
        while hapus == "":
            hapus = input("Masukkan nomor billing : ")
        hapus = int(hapus)
        b = databilling.urutan(hapus -1)
        hapusdatawarnet.tambahbilling(b.data,b.jam,b.harga)            
        databilling.hapusbilling(hapus -1)
    except:
        print("Data Tidak Ditemukan")

#fungsi untuk membayar data billing
def membayardatabilling():
    try:
        hapus =""
        while hapus == "":
            hapus = input("Masukkan nomor billing : ")
        hapus = int(hapus)
        b = user.urutan(hapus -1)      
        user.hapusbilling(hapus -1)
        print("Billing dengan nama",b.data,"durasi",b.jam,"dengan harga",b.harga,"Telah dibayar")
    except:
        print("masukkan inputan dengan benar")

#fungsi untuk menampilkan menu admin
def tampilanadmin():
    while True:
        print("===================================")
        print("=======     MENU ADMIN     ========")
        print("===================================")
        print("= # MENU                          =")
        print("= 1. Tambah Billing               =")
        print("= 2. Hapus Billing                =")
        print("= 3. Lihat Seluruh Data Billing   =")
        print("= 4. History Data Billing         =")
        print("= 5. Kembali                      =")
        print("===================================")
        pilih = input("Pilih nomor yang ingin kamu lakukan : ")
        if pilih == "1":    #menu tambah billing
            menambahdatabilling()
        elif pilih == "2": #menu menghapus data biling
            if databilling.tampildatabilling() != -1:
                menghapusdatabilling()
        elif pilih == "3":    #menu menampilkan data biling
            print("==========================")
            print("| 1. Sorting data        |")
            print("| 2. Searching data      |")
            print("==========================")
            i = ""
            while i!="1" and i!="2":
                i = input("Ingin melakukan apa? : ")
            if i == "1":
                print("Setelah di-sort :")
                databilling.tampildatabilling()
            elif i == "2":
                if databilling.tampildatabilling()!=-1:
                    nama=""
                    while nama=="":
                        nama =input("Masukan Nama : ")
                    databilling.searchs(nama)
        elif pilih == "4" :#menu history
            while True:
                print("=================================")
                print("= # MENU HISTORY                =")
                print("= 1. Billing yang terdaftar     =")
                print("= 2. Billing yang dihapus       =")
                print("= 3. Kembali ke menu awal       =")
                print("=================================")
                pilih1 = input("Masukkan nomor yang ingin dilakukan : ")
                if pilih1 == "1":#menu untuk menampilkan data biling, baik yang sudah dihapus maupun belum
                    print("List data billing yang ada")
                    tambahdatawarnet.tampildatabilling()
                elif pilih1 == "2":#menu untuk melihat data biling yang telah dihapus
                    print("List data billing yang dihapus")
                    hapusdatawarnet.tampildatabilling()
                elif pilih1 == "3":
                    break
                else:
                    print("Inputan Salah")
        elif pilih == "5": 
            break
        else :
            print("masukan inputan dengan benar")

#menu user
def tampilanuser():
    while True:
        print("===========================================")
        print("=======    MENU USER    ===================")
        print("===========================================")
        print("= # MENU                                  =")
        print("= 1. Bayar Billing                        =")
        print("= 2. Tampilkan Billing yang belum Dibayar =")
        print("= 3. Ambil Billing                        =")
        print("= 4. Kembali                              =")
        print("===========================================")
        pilih = input("Masukkan pilihan nomor yang ingin dilakukan : ")
        if pilih == "1":#menu untuk mmembayar biling yang telah diambil
            if user.print_list() != -1:
                membayardatabilling()
        elif pilih == "2":#menu yang digunakan untuk menampilkan billing yang belum dibayar
            user.print_list()
        elif pilih == "3":#menu pengambilang biling
            nama = ""
            while nama =="":
                nama =input("Masukan Nama : ")
                if nama == "":
                    print("Masukan Inputan dengan benar")
            databilling.search(nama)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid")

#menu role
def tampilan():
    while True:
        print("=================================")
        print("=======    ASD WARNET    ========")
        print("=================================")
        print("= # MENU TAMPILAN AWAL          =")
        print("= 1. Login user                 =")
        print("= 2. Login admin                =")
        print("= 3. Exit                       =")
        print("=================================")
        pilih = input("Masukkan pilihan nomor yang ingin dilakukan : ")
        if pilih == "1":#menu untuk login sebagai user
            tampilanuser()
        elif pilih == "2":#menu untuk login sebagai admin
            tampilanadmin()
        elif pilih == "3":
            print("Kamu telah keluar dari program")
            print("Terimakasih!!!")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
tampilan() 
