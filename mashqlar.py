# kocha = "Turon Zamin"
# mahalla = "Mexnatobod"
# tuman = "Qo'shko'pir"
# viloyat = "Xorazm"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha = input("Kocha nomini kiritng:")
# mahalla = input("Mahalla nomini kiritng:")
# tuman = input("Tuman nomini kiriting:")
# viloyat = input("Viloyat nomini kiritng:")
# print(f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyati")

# kocha = input("Kocha nomini kiritng:")
# mahalla = input("Mahalla nomini kiritng:")
# tuman = input("Tuman nomini kiriting:")
# viloyat = input("Viloyat nomini kiritng:")
# print(f"{kocha.title()} ko'chasi,\n {mahalla.title()} mahallasi,\n {tuman.title()} tumani,\n {viloyat.title()} viloyati\n")

# son = int(input("Istalgan son kiriting:"))
# print(f"{son} ning kvadrati {son**2} ga teng")

# yosh = int(input("Yoshingiz nechida:\n>>>"))
# t_yil = 2021-yosh
# print("Siz " + str(t_yil) + " yilda tug'ilgan ekansiz")

# son1 = int(input("Birinchi sonni kiriting:"))
# son2 = int(input("Ikkinchi sonni kiriting"))

# ismlar = ["diyor","sardor","joni"]
# print(f"Salom {ismlar[1].title()}, bugun choyxona bormi?," )
# print(f"{ismlar[2].title()} choyxonaga boramizmi?")


# t_shaxslar = ["Jaloliddi Manguberdi","Imom Buxori"]
# z_shaxslar = ["Muhammad Xoblos","Zakir Naik"]
# shaxs = t_shaxslar.pop(1)
# sshaxs = z_shaxslar.pop(0)
# print(f"Men tarixiy shaxslardan {shaxs} bilan,")
# print(f"zamonaviy shaxslardan esa {sshaxs} bilan suxbat qilishni hohlar edim")

# davlatlar = ["rassiya","mexika","tokio","danya","gorgiya"]
# print(davlatlar)

# taomlar = ['osh','norin','kabaob','dimlama','manti','sho\'rva']

# ism = ['sardor','otabark','farrukh','umurbek','diyor']
# for d in ism:
#     print(f"Salom, {d.title()}")

# kinolar = []
# print("5 ts sevimli kinolaringizni kiriting:")
# for d in range(5):
#     kinolar.append(input(f"{d+1}- kinoni kiriting:"))
# print(kinolar)

# cars = ['toyota','gm','nexia','audi','mersedes']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota','gm','nexia','audi','mersedes']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# login = input("Login ismini kiriting:")
# if login.lower()  == 'diyor':
#     print("Xush kelibsiz Admin ")
#     print("Foydalanuvchilar ro'yxatini ko'rishni istaysizmi")
# else:
#     print(f"Xush kelibsiz {login.title()}")

# son1 = int(input("1-sonni kiriting:"))
# son2 = int(input("2-sonni kiriting:"))
# if son1==son2:
#     print("Sonlar teng ekan.")
# else:
#     print("Sonlar teng emas ekan.")

# son = int(input("Istalgan son kiritng:"))
# if son<0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# son = int(input("Son kiriting")
          
# son = int(input("Juft son kiriting:"))
# if son%2==1:
#     print("Bu juft son emas")
# else:
#     print("Raxmt")

# kub = []
# for n in range(10):
#     kub.append(f"{n**3}")
# print(kub)

# cars = ['bmw','audi','volvo','gm','kia','hyundai','tesla']
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     elif car == "gm":
#         print(car.upper())
#     else:
        # print(car.title())

# son = int(input("Son kiriting:"))
# if son>0:
#     print(f"{son} ning ildizi {son**2} ga teng")
# else:
#     print("Musbat son kiritng")
    
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4:
#     print("Sizga kirish bepul.")
# elif yosh>=60:
#     print("Sizga kirish bepul.")
# elif yosh<=12:
#     print("Sizga kirish 5000 so'm.")
# elif yosh<=18:
#     print("Sizga kirish 8000 so'm.")
# else: 
#     print("Sizga kirish 10000 so'm.")

# son1 = int(input("1-sonni kiriting:"))
# son2 = int(input("2-sonni kiriting:"))
# if son1>=son2:
    # print()

# maxsulotlar = ['olma','go\'sht','piyoz','karam','nok','ananas','sabzi','un','guruch']
# savat = []
# print("5 ta maxsulot buyurtma qiling.")
# for n in range(5):
#     savat.append(input(f"{n+1}-maxsulot nomini kiriting: "))
# for zakaz in savat:
#     if zakaz in maxsulotlar:
#         print(f"Do'konda {zakaz} bor ")
#     else:
#         print(f"Do'konda {zakaz} yo'q.")

# otam = {'ism':'murod','t_yil':1976,'t_joy':'xorazm'}
# onam = {'ism':'shaxlo','t_yil':1982,'t_joy':'xorazm'}
# ukam = {'ism':'salohiddin','t_yil':2009,'t_joy':'xorazm'}
# print(f"Otamaning ismi {otam['ism'].title()} {otam['t_yil']}-yil {otam['t_joy'].title()} viloyatida tug'ulgan")
# print(f"Onamaning ismi {onam['ism'].title()} {onam['t_yil']}-yil {onam['t_joy'].title()} viloyatida tug'ulgan")
# print(f"Ukamaning ismi {ukam['ism'].title()} {ukam['t_yil']}-yil {ukam['t_joy'].title()} viloyatida tug'ulgan")

# otam = {'ism':'otam','taom':'osh'}
# onam = {'ism':'onam','taom':'gumma'}
# ukam = {'ism':'ukam','taom':'somsa'}
# print(f"{otam['ism'].title()}ning sevimli taomi {otam['taom']} ")
# print(f"{onam['ism'].title()}ning sevimli taomi {onam['taom']} ")
# print(f"{ukam['ism'].title()}ning sevimli taomi {ukam['taom']} ")

# python = {'else':'agar','list':'ro\'yxat','intger':'butun son','str':'matn'}
# soz = input("Kalit so'zni kiriting.")
# for maxs in python:!!!!!!!!!!!!!!!
#     if maxs in soz:
#         print(f"{maxs.title()}-{python[maxs].title()}.")
#     else:
#         print("Lug'atda bunday so'z yo'q")
        
# python = {'else':'agar','list':'ro\'yxat','intger':'butun son','str':'matn'}
# soz = input("Kalit so'zni kiriting:")
# if soz in python:
#     print(f"{soz.title()}-{python[soz].title()}.")
# else:
#     print("Lug'atda bunday so'z yo'q")

# dell = {'list':'ro\'yxat','else':'agar','intger':'butun son','str':'matin'}
# for n in sorted(dell):
#     print(f"{n.title()}-{dell[n].title()}.")

# davlatlar = {
#     'aqsh':'washington',
#     'italya':'rim',
#     'malaziya':'kuala lumpur',
#     'o\'zbekiston':'toshkent',
#     'rassiya':'maskva',
#     'france':'paris'
#     }
# davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? ")
# if davlat in davlat.lower():
#     print(f"{davlat.title()}ning poytaxti {davlatlar[davlat].title()}.")
# else:
    # print("Kechirasiz bizda bu haqida ma'limot yo'q.")
    
# shaxslar = {
#     'abdulla':{'familya':'qodriy',
#               't_yil':1894,
#               't_joy':'toshkent',
#               'y_yil':44              
#               },   
#     'erkin':{'familya':'vohidov',
#               't_yil':1936,
#               't_joy':'farg\'ona',
#               'y_yil':80}
#               }
# for ism, info in shaxslar.items():
#     print(f"{ism.title()} {info['familya'].title()}, "
#           f"{info['t_yil']}-yilda {info['t_joy']}da tavvalud topgan."
#           f"{info['y_yil']}-yil umr kechirgan ")

# kitoblar = []
# n=1
# while True:
#     savol = "Eng yoqtirgan kitoblaringiz nomini kiriting:"
#     kitob = input(savol)
#     kitoblar.append(kitob)
#     takrorlash = input("Yana kitob qo'shasizmi? (stop)")
#     n+=1
#     if takrorlash.lower() == "stop":
#         break
# print("Yoqtirgan kitoblaringiz  ro'yxati:")
# for kitob in kitoblar:
#     print(kitob.title())

# savol = "Yoshingizni kiriting:"
# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == 'exit' or qiymat.lower() == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narx = 2000
#     elif 7<=yosh<18:
#         narx = 3000
#     elif 18<=yosh<65:
#         narx = 10000
        
#     else: narx = 0 
    
#     if narx == 0:
#         print("Sizga chipta bepul.")
#     else:
#         print(f"Chipta {narx} so'm.")
# print("Dastur to'xtadi")

# sonlar = []
# print("4 ta son kiriting:")
# for n in range(4):
#     sonlar.append(input(f"{n+1}-sonni kiriting:"))
# print(f"Ro'yxatdagi eng kichik son {min(sonlar)}")

# print("Kiritlgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower()=='exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtadi")

# print("Maxsulotlar va ularning norxlarini saqlaymiz")
# e_bozor = {}
# ishora = True
# while ishora:
#     maxsulot = input("Maxsulot nomini kiriting:")
#     narx = input(f"{maxsulot.title()}ning narxini kiriting:")
#     e_bozor[maxsulot]= int(narx)
#     javob = input("Yana maxsulot qo'shasizimi(ha\yo'q)")
#     if javob.lower()=="yo'q":
#         ishora = False
# for maxsulot, narx in e_bozor.items():!!!!!!!!!!!!!!!!!!
#     print(e_bozor)

# def yosh_hisobla(ism, yosh, joriy_yil=2021):
#     """Foydalanuchi yoshini kiritganda,
#     qachon tug'ulganligini hisoblavchi funksiya"""
#     print(f"{ism.title()} siz {joriy_yil-yosh} yilda tug'ulgan ekansiz.")
# ism = input("Ismingizni kiriting:")
# yosh = int(input("Yoshingizni kiriting:"))
# yosh_hisobla(ism, yosh)

# def kvadrat_kub_hisobla(son):
#     """Foydalanuvchi kiritgan son
#     kvadrati va kubini hisoblovchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi esa {son**3} ga teng.")
# hisob = int(input("Son kiriting:"))
# kvadrat_kub_hisobla(hisob)

# def sonni_tekshir(son):
#     """Foydalanuvchi kiritgan son juft yoki toq
#     ekanligin chiqaruvchi funksiya"""
#     if son%2==0:
#         print("Juft son ekan")
#     else:
#         print("Toq son ekan")
# son1 = int(input("Son kiriting:"))     
# sonni_tekshir(son1)

# def katta_kichik(son):
#     """Foydalanuvchi kiritgan sonlarning 
#     eng kattasini chiqaruvchi funksiya"""
#     print(f"Eng katta son {katta}.")
# son1 =  int(input("1-sonni kiriting:"))
# son2 = int(input("2-sonni kiriting:"))
# katta = max(son1,son2)
# katta_kichik(katta)

# def kvadrat_hisobla(son):
#     """Foydalanuvchi kiritgan sonni kvadratini hisoblaydi"""
#     print(f"{javob}")
# x = int(input("Sonni kiriting:"))
# y = 2
# javob = f"{x**y}"
# kvadrat_hisobla(javob)
    

# def hodim_haqida(ismi, familyasi, tugilgan_yili, tugilgan_joyi, yoshi, email_manzili=None, telefon_raqami=None): 
#     malumotlar = {'ism':ismi,
#                   'familya':familyasi,
#                   'tugilgan_yil':tugilgan_yili,                
#                   'tugilgan_joy':tugilgan_joyi,
#                   'yosh':yoshi,
#                   'email_manzil':email_manzili,
#                   'telefon_raqam':telefon_raqami}
#     return malumotlar
# print("Hodimlar haqida malumotlarni shakillantiramiz.")
# malumott = []
# while True:
#     print("\nQuyidagi malumotlarni kiriting", end='')
#     ismi = input("Hodim ismi: ")
#     familyasi = input("Hodim familyasi: ")
#     tugilgan_yili = input("Tug'ilgan yili: ")
#     tugilgan_joyi = input("Tug'ilgan joyi: ")
#     yoshi = input("Yoshi: ")
#     email_manzili = input("Email manzili: ")
#     telefon_raqami = input("Telefon raqami: ")
#     malumott.append(hodim_haqida(ismi, familyasi, tugilgan_yili, tugilgan_joyi, yoshi, email_manzili, telefon_raqami))
#     javob = input("Yana malumot qo'shasizmi(yes|no):")
#     if javob == "no":
#         break
# print("\nKampaniya hodimlar haqida malumotlar: ")
# print(hodim_haqida)
# for malumotlar in malumott:
#     if malumotlar["email_manzil"]:
#         email_manzil = malumotlar['email_manzil']
#     elif malumotlar["telefon_raqam"]:
#         telefon_raqam = malumotlar['telefon_raqam']
#     else:
#         email_manzil = "Noma'lum"
#         telefon_raqam = "Noma'lum"
#     print(f"{malumotlar['ism'].title()} {malumotlar['familya'].title()} {malumotlar['tugilgan_yil'].title()}-yil  {malumotlar['tugilgan_joy'].title()} viloyatida tug'ilgan {malumotlar['yosh']} yoshda Email mazil: {malumotlar['email_manzil']} Tel: {malumotlar['telefon_raqam']}")

# def katta_son_chiqar(son):
#     """Foydalanuvchi kiritgan sonlarning
#     eng kattasin chiqaruvchi funksiya"""
#     print(f"Eng katta son {max_qiymat}")
# sonlar = []
# for n in range(3):
#     sonlar.append(int(input(f"{n+1}-sonni kiriting: ")))
# max_qiymat = max(sonlar)
# katta_son_chiqar(max_qiymat)

# def lugat_chiqar(radius, diametr, uzunlig):
#     lugat = {'radius':radius,
#               'diametr':diametr,
#               'uzunlig':uzunlig}
#     return lugat
# print("Hisoblaymiz")
# radius = int(input("Radiusni kiriting: "))

# def katta_harf(ismlar):
#     for ism in ismlar:
#         print(f"{ism.title()}")
# nom =  ['olim','ali','anvar','karim','diyor']
# ismlar = nom[:]
# katta_harf(ismlar)

# def katta_harf(ismlar):
#     for ism in ismlar:
#         print(f"{ism.title()}")
# nom =  ['olim','ali','anvar','karim','diyor']
# ismlar = nom[:]
# katta_harf(ismlar)

# def qoshilma(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# print(qoshilma(1,2))
# print(qoshilma(1,2,3,4,5))
# print(qoshilma(4,5,6,7))
# print(qoshilma(1))

# def malumotlar(ism,familya,**malumot):
#     """Talabalar haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumot['ism']=ism
#     malumot['familya']=familya
#     return malumot
# talaba0 = malumotlar('diyor','qurbonboyev',t_yil=2003,yosh=18)
# talaba1 = malumotlar("sardor","dushamov",t_yil=2003,yosh=18)