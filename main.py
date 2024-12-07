# 1 vazifa


# import random
# from decimal import Decimal
#
#
# class ValueError(Exception):
#     def __init__(self,message):
#         self.message = message
#
# class Check_USD:
#     def __set_name__(self, owner, name):
#         self.name = name
#     def __set__(self, instance, value):
#         if type(value) == Decimal:
#             instance.__dict__[self.name]=value
#         else:
#             raise ValueError("Qiymat xato kiritildi!!")
#
#     def __get__(self, instance, owner):
#         return  instance.__dict__[self.name]
#     def __delete__(self, instance):
#          del instance.__dict__[self.name]
#
# class USD:
#     usd = Check_USD()
#     def __init__(self,usd: Decimal):
#         self.usd = usd
#     def random(self):
#         c = ["2024.12.21", "2024.12.09", "2024.12.01", "2024.12.05"]
#         b = random.choice(c)
#         return b
#     def Konvertatsiya(self):
#         """
#         1 USD = 12000 so'm.
#         """
#         a = self.usd * 12000
#         return (f"USD -> UZS konvertatsiya qilishda 1 USD = 12,000 UZS koeffitsiyenti ishlatildi!\n"
#                 f"{a} UZS sana: {p1.random()}" )
# usd = Decimal(input("Usd kiritng: "))
# p1 = USD(usd)
# print(p1.Konvertatsiya())

# 2 vazifa

import random
from decimal import Decimal


class ValueError(Exception):
    def __init__(self,message):
        self.message = message


class Check_Price:
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, instance, value):
        if type(value) == Decimal:
            if value > 0:
                 instance.__dict__[self.name]=value

            else:
                raise ValueError("Qiymat xato kiritildi!!")
        else:
            raise ValueError("Qiymat xato kiritildi!!")

    def __get__(self, instance, owner):
        return  instance.__dict__[self.name]
    def __delete__(self, instance):
         del instance.__dict__[self.name]

class Mahsulot:
    def __init__(self, narx):
        self.narx = narx
    def sana(self):
        c = ["2024.12.21", "2024.12.09", "2024.12.01", "2024.12.05"]
        b = random.choice(c)
        return b
    def cheginma(self):
        a = random.randint(1,50)
        javob =  self.narx - self.narx * a /100
        return (f"Maxsulot narxi: {self.narx}, chegirma: {a}\n"
                f"Chegirmadagi narx: {javob} Sana: {p1.sana()}")


narx = Decimal(input("Maxshlot narxini kiriting: "))
p1 = Mahsulot(narx)
print(p1.cheginma())