from prettytable import PrettyTable
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
                
class LinkedList:
    def __init__(self):
        self.head = None
    
    def tambahbilling(self, value):
        if self.head is None:
            self.head = Node(value)
        else: 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
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
    def urutan(self, index):
        current_node = self.head
        current_index = 0

        while current_node is not None:
            if current_index == index:
                return current_node

            current_node = current_node.next
            current_index += 1
            
    def tampildatabilling(self):
        if self.head is None:
            print("Tidak ada billing")
        else :
            tabelbilling = PrettyTable()
            tabelbilling.field_names = ["No", "Nama Billing"]
            n = self.head
            a = 1
            while n is not None:
                tabelbilling.add_row([a, n.data])
                a += 1
                n = n.next
                print(tabelbilling)
    
class linkedlist_menambahdatabilling:
    def __init__(self):
        self.head = None
    
    def tambahbilling1(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def tampildatabilling1(self):
        if self.head is None:
            print("Tidak ada billing")
        else :
            tabelbilling = PrettyTable()
            tabelbilling.field_names =  ["No", "Nama Billing"]
            n = self.head
            b = 1
            while n is not None:
                tabelbilling.add_row([b, n.data])
                b += 1
                n = n.next
            print(tabelbilling)
            
class linkedlist_menghapusdatabilling:
    def __init__(self):
        self.head = None
    
    def tambahbilling2(self, value):
        if self.head is None :
            self.head = Node(value)
        else : 
            nodebaru = Node(value)
            nodebaru.next = self.head
            self.head = nodebaru
    
    def tampildatabilling2(self):
        if self.head is None:
            print("Tidak ada billing")
        else :
            tabelbilling1 = PrettyTable()
            tabelbilling1.field_names = ["No", "Nama Billing"]
            n = self.head
            c = 1
            while n is not None:
                tabelbilling1.add_row([c, n.data])
                c += 1
                n = n.next
                print(tabelbilling1)
                
databilling = LinkedList()
tambahdatawarnet = linkedlist_menambahdatabilling()
hapusdatawarnet = linkedlist_menghapusdatabilling()

def menambahdatabilling():
    inputA = input("Masukkan nama billing baru : ")
    password = input("Masukkan password baru : ")
    databilling.tambahbilling(inputA)
    tambahdatawarnet.tambahbilling1(inputA)
def menghapusdatabilling():
    try:
        hapus = int(input("Masukkan nomor billing : "))
        b = databilling.urutan(hapus -1)
        hapusdatawarnet.tambahbilling2(b.data)            
        databilling.hapusbilling(hapus -1)
    except:
        print("masukkan inputan dengan benar")

while True:
    print("===================================")
    print("=======     ASD WARNET     ========")
    print("===================================")
    print("= # MENU                          =")
    print("= 1. Tambah Billing               =")
    print("= 2. Hapus Billing                =")
    print("= 3. Lihat Seluruh Data Billing   =")
    print("= 4. History Data Billing         =")
    print("= 5. Exit                         =")
    print("===================================")
    pilih = input("Pilih nomor yang ingin kamu lakukan : ")
    if pilih == "1":    
        menambahdatabilling()
    elif pilih == "2":
        databilling.tampildatabilling()
        menghapusdatabilling()
    elif pilih == "3":    
        databilling.tampildatabilling()
    elif pilih == "4" :
        while True:
            print("===================================")
            print("= # MENU HISTORY                  =")
            print("= 1. Billing yang terdaftar       =")
            print("= 2. Billing yang dihapus         =")
            print("= 3. Kembali ke menu awal         =")
            print("===================================")
            pilih1 = input("Masukkan nomor yang ingin dilakukan : ")
            if pilih1 == "1":
                print("List data billing yang ada")
                tambahdatawarnet.tampildatabilling1()
            elif pilih1 == "2":
                print("List data billing yang dihapus")
                hapusdatawarnet.tampildatabilling2()
            elif pilih1 == "3":
                break
            else:
                print("Input Salah")
    elif pilih == "5":
        print("Kamu telah keluar dari program")
        print("Terimakasih!!!")
        exit()
    else :
        print("masukan inputan dengan benar")