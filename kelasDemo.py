class Demo(object):
    def __init__(self, m,p,a):
        self.mahasiswa = m
        self.pelajar = p
        self.aparat = a

    def hitungJumlah(self):
        return self.mahasiswa + self.pelajar +  self.aparat

    def cetakData(self):
        print("mahasiswa\t: ",self.mahasiswa)
        print("pelajar\t: ",self.pelajar)
        print("aparat\t: ",self.aparat)

    def cetakJumlah(self):
        print("Jumlah Massa\t: ", self.hitungJumlah())

class DemoDpr(Demo):
    def __init__(self, m,p,a,d):
        self.mahasiswa = m
        self.pelajar = p
        self.aparat = a
        self.dpr = d

    def cetakData(self):
        print("mahasiswa\t: ",self.mahasiswa)
        print("pelajar\t: ",self.pelajar)
        print("aparat\t: ",self.aparat)
        print("dpr\t: ",self.dpr)

def main():
    DemoDpr1 = DemoDpr(1000,500,400,"Tolak KUHP")
    DemoDpr1.cetakData()
    DemoDpr1.cetakJumlah()

if __name__ == "__main__" :
   main()
