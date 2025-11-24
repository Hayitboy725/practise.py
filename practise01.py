# talaba_1 = {
#     'ism':'Hayitboy',
#     'familya':'hayiboyev',
#     'yosh':18,
#     't_yili':2007
# }
# print(talaba_1['ism'])
# print(talaba_1['familya'])
# print(talaba_1.items())


# for j,n in talaba_1.items():
#     print(f"Kalit: {j}")
#     print(f"Value:{n} \n")


# telefonlar = {
#     'ali':'galaxy x',
#     'hayitboy':'samsung',
#     'abror':'redmi',
#     'shahzod':'iphone'
# }

# for g ,q in telefonlar.items():
#     print(f"{g.title()}ning telefoni {q.title()}")


# mahsulotlar = {
#     'olma':10000,
#     'anor':12000,
#     'anjir':1500,
#     'banan':20000
# }


# print(mahsulotlar.keys())

# for j in mahsulotlar:
#     print(j.title())

# bozorlik = {'uzum','anor','banan','orik'}
# for j in mahsulotlar:
#     if j in bozorlik:
#         print(f"{j.title()} {mahsulotlar[j]}so'm")
# for g in bozorlik:
#     if g not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {g}ni ham olib keling")


# print("dokonimizdagi mahsulotlar")
# for l in sorted(mahsulotlar):
#     print(l.title())

# print(mahsulotlar.values())
# for w in mahsulotlar.values():
#     print(w)
# print(type(mahsulotlar))
# print(mahsulotlar)


# toys = {'car','banan','car','gear','banan','ball','ball'}


# print(type(toys))
# print(toys)

# sozlar = {'book':'kitob','car':'moshina','world':'dunyo', 'mobile':'telefon','computer':'notbook'}
# for j,k in sorted(sozlar.items()):

#     print(f"{j}-{k}")


davlatlar ={
    'ozbekiston':'toshkent',
    'rossiya':'moskva',
    'yaponiya':'tokyo',
    'xitoy':'pekin',
    'brazilya':'brazil',
    'amerika':'vashington',
    'saudiya arabistoni':'riyod',
    'qatar':'doha'
}
# print(sorted(davlatlar.keys()))

# print(sorted(davlatlar.values()))
# for i in sorted(davlatlar):
#     print(i.title())
# for g in sorted(davlatlar.values()):
#     print(g.title())

# a = input("Istalagan davlat kiriting: ")
# b = davlatlar.get(a)

# if b == None:
#     print("kechirasz bizda bunday malumot yo'q")
# else:
#     print(f"{a.upper()} ning poytaxti {b} shahri")



menyu = {
    'palov':10000,
    'shorva':12000,
    'shavla':15000,
    'makron':17000,
    'somsa':20000,
    'shahsli':22000,
    'manti':25000,
    'mastava':300000,
    'oliviya':8000,
    'tuxum barak':45000
}
buyurtmalar =[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())


for buyurtma in buyurtmalar:
    if buyurtma in menyu:
        print(f"{buyurtma.title()} ning narxi {menyu[buyurtma]} so'm")
    else:
        print("bizda bunday ovat yoq")
