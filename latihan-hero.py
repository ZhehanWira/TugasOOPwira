print(" LATIHAN 1: CLASS & OBJECT ")

class Hero:
    # Constructor
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Method info
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    # LATIHAN 2: Method serang
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# Main Program
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)
hero3 = Hero("Angela", 340, 40)

hero1.info()
hero2.info()
hero3.info()

hero1.hp = 500
print(hero1.hp)

# ANALISIS LATIHAN 1
# Jika hero1.hp diubah menjadi 500, maka nilai HP hero1 berubah
# karena attribute bersifat public dan dapat diubah langsung.


print("\n LATIHAN 2: INTERAKSI ANTAR OBJECT ")
print("--- Pertarungan Dimulai ---")

hero1.serang(hero2)
hero2.serang(hero1)

# ANALISIS LATIHAN 2
# Parameter lawan menerima object, bukan string
# sehingga object dapat memanggil method object lain.


print("\nLATIHAN 3: INHERITANCE")

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} menggunakan Fireball!")
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana tidak cukup")


eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.skill_fireball(balmond)

# ANALISIS LATIHAN 3
# super() digunakan untuk memanggil constructor class induk
# Tanpa super(), attribute dari Hero tidak akan terbentuk.

print("\n LATIHAN 4: ENCAPSULATION ")

class HeroSafe:
    def __init__(self, name, hp_awal):
        self.name = name
        self.__hp = hp_awal  # private

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai):
        if nilai < 0:
            self.__hp = 0
        elif nilai > 1000:
            self.__hp = 1000
        else:
            self.__hp = nilai


hero_safe = HeroSafe("Layla", 100)
hero_safe.set_hp(-50)
print("HP:", hero_safe.get_hp())

# ANALISIS LATIHAN 4
# Attribute __hp bersifat private
# Getter dan setter menjaga agar data tetap valid.

print("\n LATIHAN 5: ABSTRACTION & INTERFACE ")

from abc import ABC, abstractmethod

class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class HeroUnit(GameUnit):
    def __init__(self, name):
        self.name = name

    def serang(self, target):
        print(f"Hero {self.name} menyerang {target}")

    def info(self):
        print(f"Saya Hero {self.name}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}")

    def info(self):
        print(f"Saya Monster {self.jenis}")


h = HeroUnit("Alucard")
m = Monster("Serigala")

h.info()
m.info()

# ANALISIS LATIHAN 5
# Abstract class tidak bisa dibuat object
# Semua class turunan wajib mengimplementasikan method abstrak.

print("\n LATIHAN 6: POLYMORPHISM")

class HeroPoly:
    def __init__(self, name):
        self.name = name

    def serang(self):
        print("Hero menyerang biasa")


class MagePoly(HeroPoly):
    def serang(self):
        print(f"{self.name} menembakkan bola api!")


class Archer(HeroPoly):
    def serang(self):
        print(f"{self.name} memanah dari jauh!")


class Fighter(HeroPoly):
    def serang(self):
        print(f"{self.name} menyerang dengan pedang!")


pasukan = [
    MagePoly("Eudora"),
    Archer("Miya"),
    Fighter("Zilong")
]

for pahlawan in pasukan:
    pahlawan.serang()

# ANALISIS LATIHAN 6
# Satu method yang sama menghasilkan perilaku berbeda
# Polymorphism membuat program fleksibel dan mudah dikembangkan.

