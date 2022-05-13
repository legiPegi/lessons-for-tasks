# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# ismlar = ["Ali", 'Vali', 'Shokir']
# for ism in ismlar:
#     print(f"Assalomu aleykum {ism}")
# print(f"Kod {len(ismlar)}")
# a = list(range(1, 1000, 2))
# print(a)

# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)

# a = list(range(1, 100, 2 ))
# for b in a:
#     print(f"{b}-ning kvadrati {b**2}")

# b = input("Salom ismingizni kiritng >>> ")
# if b.lower() != 'ali':
#     print(f"uzr {b.title()} biz Alini") 
# else:
#     print("Salom Ali")
    
    
# cars = ['audi', 'ferrari', 'bugatti', 'gm', 'lasetti']
# for car in cars:
#     if car != 'gm':
#         print(car.lower())
#     else:
#         print(car.upper())


# a = "Ali"
# b = input("Salom ism kiriting >>> ")
# if b != a.lower():
#     print(f"Salom {b.title()} xush kelibsiz")
# else:
#     print("Salom Admin xush kelibsiz")
    
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting:"))
# if x==y: print(f"Sonlar teng: {x}={y}")
# else: print("Yaxshi")
    
    

# son = float(input('Istalgan son kiriting: '))
# if son>0:
#     print(son**(1/2))
# else: 
#     print('Musbat son kiriting')



# login = "Ali"
# parol = 12345
# a = input("Login ")
# b = int(input("parol "))
# if a == login.lower() and b == parol:
#     print("Salom xush kelibsiz")
# else:
#     print("Login yoki parol xato")    


# a = 17
# b = a%2 toq yoki juft
# print(b)

# a = int(input("Juft son kiriting 1>> "))
# if a%2:
#     print("Siz toq son kiritdingiz ")
# else:
#     print("Raxmat")


# a = int(input("Salom bizning Milliy muzeyga hush kelibsiz kirish\
# bahosi yoshingizni ko'rsatsangiz aytamiz\
#  iltimos yoshingizni kiriting>>> "))
# if a<=4:
#     narh = 0
# elif a<=8:
#     narh = 4000
# elif a<=12:
#     narh = 8000
# else:
#     narh = 15000
# print(f"Sizga kirish narhi {narh} so'm")

# son1 = int(input("1-son>> "))
# son2 = int(input("2-son>> "))
# if son1 == son2:
#     print("Sonlar bir xil")
# elif son1>son2:
#     print(f"{son1} katta {son2} dan")
# else:
#     print(print(f"{son1} kichik {son2} dan"))
 



   
# mahsulotlar = ['anor', 'uzum', 'nok', 'shaftoli',\
# 'banan', 'olma', 'bodring', 'pomidor', 'gilos', 'qulupnay']

# print("Salom do'konimizga hush kelibsiz\
# eng kamida 5ta mahsulot tanlang")

# savat = []
# for a in range(5):
#     savat.append(input(f"Savatga  {a+1} maxsulotini tanlang "))

# for b in savat:
#    if b in mahsulotlar:
#        print(f"{b} mahsuloti bizda bor")
#    else:
#     print(f"{b} yoq")           


# mahsulotlar = ['anor', 'uzum', 'nok', 'shaftoli',\
# 'banan', 'olma', 'bodring', 'pomidor', 'gilos', 'qulupnay']

# mahsulot = []

# bor = []
# yoq = []
# for a in range(3):
#     mahsulot.append(input(f"{a+1}-mahsulot "))
    
# for k in mahsulot:
#     if k in mahsulotlar:
#         bor.append(k)
#     else:
#         yoq.append(k)

# if yoq:
#     print("Xozir shu maxsulotlar yoq qolgan barcha\
# maxsulotlar bor ")
#     for n in yoq:
#         print(n)
# else:
#     print("Barchasi bor")

# foydalanuvchilar = ["anvar", 'odil', 'legi', 'zorro', 'king']
# b = input("Iltimos ismingiz >> ")
# print(f"Salom {b.title()}")
# a = input("Yangi login kiriting>>> ")
# if a in foydalanuvchilar:
#     print("Uzr bu login band qilingan boshqa login tanlang ")
# else:
#     print(f"Tabriklaymiz {b.upper()}jon siz royhatdan otdingiz ")
#     print(f"Sizning yangi loginingiz {a} yodingizdan chiqarmang")
    



############ 1   ###########
# print("Salom tugilgan yilingizni xisoblovchi")
# t_yil = "Tugilgan yilingizni kiriting"
# t_yil += "(Dasturni toxtatish uchun '1'ni bosing )>>> "
# yil = ''
# while yil != 1:
#     yil = input(t_yil)
#     yil = int(yil)
#     if yil != 1:
#         print(2022-yil)
#     else:
#         print('Dastur toxtadi')
        
        
    ################## 2  #########################

# print("Salom tugilgan yilingizni xisoblovchi")
# t_yil = "Tugilgan yilingizni kiriting"
# t_yil += "(Dasturni toxtatish uchun '1'ni bosing )>>> "
# stop = True
# while stop:
#     a = input(t_yil)
#     a = int(a)
#     if a == 1:
#         stop = False
#     else:
#         print(f"Siz {2022-a} yoshdasiz")
# print('Dastur toxtadi')

 
# print("Salom Hush kelibsiz !!!")
# t_yil = "Parolni kiriting "
# ism = input("Ismingizni kiritng>>> ")
# print(f"Hurmatli {ism.title()} endi")
# b = 1234
# # stop = True
# while True:
#     a = input(t_yil )
#     a = int(a)
#     if a == b:
#         break
#     else:
#         print(f"Uzr {ism.title()} parolni xato kiritdingiz qayta kiriting ")
# print("Admin profile is activated ")
# c = 1
# while c <= 20:
#     c += 1
#     print(c * '*')    
# input()   
        
    
############################################################
# son = 0
# while son<10:
#     son += 1
#     if son%2 != 0: ### agar son qoldigi yoq bolsa yani juft bolsa chiqarad
#         continue
#     else:
#         print(son)
    
##########################################################

# son = 0
# while son<10:
#     son += 1
#     if son%2 == 0: ### agar son qoldigi bor bolsa yani toq bolsa chiqarad
#         continue
#     else:
#         print(son)


# a = "Yoqtirgan kitoblaringizni kiriting"
# a += "(Agar dasturni\
# to'xtatmoqchi bo'lsangiz 1 ni bosing)>>> "
# while True:
#     c = input(a)
#     if c == '1':
#         break
# print("Dastur tugadi")    


# print("Assalomu aleykum Milliy muzeyga hush kelibsiz !!!")
# yosh = "Iltimos yoshingizni kiriting"
# yosh += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing)>> "
# yosh = "Yosh kiriting "
# while True:
#     a = input(yosh)
#     if a == 'exit' or a == 'quit': 
#         break
    
#     a = int(a)
    
#     if a <= 7:
#         narh = 2000
    
#     elif 7<a<14:
#         narh = 8000
    
#     elif 14<=a<18:
#         narh = 15000
   
#     elif 18<=a<50:
#         narh = 20000
   
#     else:
#         narh = 0
    
#     if narh == 0:
#         print("Sizga kirish bepul")
#     else:
#         print(f"sizga kirish narhi{narh}so'm")

#################################################
    
# yosh = "Yosh kiriting "
# stop = True
# while stop:
#     a = input(yosh)
#     if a == '999' or a == '555': 
#         stop = False
   
#     a = int(a)
    
#     if a == '999' or a == '555':
#         a = str(a)
    
#     if a <= 7:
#         narh = 2000
    
#     elif 7<a<14:
#         narh = 8000
    
#     elif 14<=a<18:
#         narh = 15000
   
#     elif 18<=a<50:
#         narh = 20000
   
#     else:
#         narh = 0
    
#     if narh == 0:
#         print("Sizga kirish bepul chunki sizni yoshingiz\
#   50 dan katta ekan bizda 50 yoshdan yuqoridagilarga kirish bepul")
#     else:
#         print(f"sizga kirish narhi {narh}-so'm")
# print("Dastur tugadi")

a = "yosh"
stop = True
while stop:
    b = input(a)
    if b != 'exit':
        print(b)
        continue
    else:
        stop = False
print("tugadi")        
    










