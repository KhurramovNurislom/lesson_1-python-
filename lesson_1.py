# print("asdasd")
# False
# if 5 > 2:
#      print ("Five is greater than two!")

# True
# if 5 > 2:
#     print("Five is greater than two!")

# if 5>2:
#     print("Five is greater than two!")

# if 5 > 2:
#         print("Five is greater than two!")

# #Sharhalar

# """
# sdfsdfsdf
# """

# print("hello")

# x=5
# y = "John"
# print(x)
# print(y)


# x=3  
# y = "Sally"
# print(x)
# print(y)

# x = str(3)
# y=int(3)
# z=float(3)

# print(type(x))
# print(type(y))
# print(type(z))


# print("asdas")
# _MY_var = "John"
# _MYvar = "ad"

# print(_MY_var)
# x, y, z = "1q", "2q", "3q"

# print(x, y, z)

# fruits = ["q2", "q3", "q4"]
# x1, y1, z1 = fruits
# print(x1, y1, z1)


# x = "awesome"


# def myfunc():
#     print(10>9)
#     print(10==9)
#     print(10<9)

# myfunc()

# x="awesome"
# def myfunc():
#     global x
#     x = "fantastic"
# myfunc()

# print("Python is " + x)

# bool = True
# print(bool)


# x1 = 1j
# print(x1)

# x2 = ["apple", "banana", "cherry"]
# print(x2)

# x3 = ("apple", "banana", "cherry")
# print(x3)

# x4 = range(6)
# print(x4.index(5))

# x5 = {"apple":"banana", "age":36}
# print(x5.get("age"))

# import random
# print(random.randrange(10,150))

# a = "adsajskbhlkjbbashkfvggklhjabdlskkfjjhbkasdfsg"
# for x in a:
#     print(x)
#     print(len(a))

# age = 36
# txt = "My name is John, and I am {}, is it  years old?"
# print(txt.format(age))

# print (5**4)
# print (5^4)


buyruqSanasi = input("buyruq sanasini kiriting: ")
buyruqSoni = input("buyruq soni kiriting: ")
buyruqRaqami = input("buyruq raqamini kiriting: ")
xodimFullName = input("Xodimning to'liq familiyasi, ismi va otasining ismi: ")

xodimWorkTime = input("Xodimning korxonada ishlagan vaqt oralig'i: ")
xodimFromTime = input("Ta'til boshlanishi vaqti: ")
xodimToTime = input("Ta'til tugash vaqti: ")

xodimHolidayTime = input("Xodimga navbatdan oldin berilgan yillik mehnat ta'tili vaqt: ")

rahbatFullName = input("Tashkilot rahbari imzosi va familiyasi, ismi va otasining ismi: ")

ariza = """


                                          B U Y R U Q

        {}               {}-son                 №:{}.

        
            Navbatdan oldin yillik mehnat ta'tili berish to'g'risidagi

    {}, ismi va otasining ismiga o'n to'rt yoshga to'lmagan ikki
nafar bolali yolg'iz ona bo'lganligi sababli uning xohishiga ko'ra navbatdan oldin {}dan
{}gacha haqiqatda {} - yillarda ishlagan vaqti uchun Xodimga
{} ish kunidan iborat navbatdagi mehnat ta'tili berilsin.



    Bosh buxgalterga: tegishli to'lovlarni amalga oshirsin.


    Asos:  {}ning arizasi, O'zbekiston
Respublikasi Mehnat Kodeksining 216, 228-moddalari, 2023-yil uchun ta'tillar jadvali.

   
    
    Tashkilot rahbari                               {}                                    
   
                                                                        
    Buyruq bilan tanishdim                       {}
                                            
                                            """
print(ariza.format(buyruqSanasi,buyruqSoni,buyruqRaqami,xodimFullName,xodimFromTime,xodimToTime,xodimWorkTime,xodimHolidayTime,xodimFullName,rahbatFullName,xodimFullName))






