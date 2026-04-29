#2-misol
class Talaba:
    def __init__(self, ism, kurs, baholar):
        self.ism = ism
        self.kurs = kurs
        self.baholar = baholar

    def malumot(self):
        print(f"Ismi: {self.ism}")
        print(f"Kursi: {self.kurs}")
        print(f"Bahosi: {self.baholar}")

    def orta_baho(self, baholar):
        if baholar > 0:
            self.baholar = baholar
        else:
            print(f"Xatolik yuz berdi")

t1 = Talaba("Dilnura", 1, 5)
t1.malumot()
print()

t1.malumot()
