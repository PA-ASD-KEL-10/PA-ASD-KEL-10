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
