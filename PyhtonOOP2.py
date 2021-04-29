class isci()

    maawi_qaldirmaq = 1.05

    per_sayi = 0


    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.email = self.ad + self.soyad + "@mediagroup.com"
        isci.per_sayi = isci.per_sayi + 1
    def tamad(self):
        return "adi : {}\nsoyadi : {}\nmaasi : {}\nemail : {}".format(self.ad, self.soyad, self.maas, self.email)


    def artir(self):
        self.maas = (self.maas*self.maawi_qaldirmaq)

personel1 = isci("Nail", "Rzayev", 2000)
print(isci.per_sayi)
personel2 = isci("Samil", "Mirzayev", 5000)
print(isci.per_sayi)

print(personel1.maas)
personel1.artir()
print(personel1.maas)


print(personel2.maas)
personel2.maawi_qaldirmaq = 1.1
personel2.artir()
print(personel2.maas)


print(isci.tamad(personel1))
print("*********************************")
print(isci.tamad(personel2))
