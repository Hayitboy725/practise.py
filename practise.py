#book_1={'Genre':'fantastic','Rang':'qizil'}
#print(book_1['Genre'])
#print(book_1['Rang'])


talaba_1 = {'ism':'hayitboy','yosh':18,'kurs':3}
print(f"{talaba_1['ism'].title()} {talaba_1['yosh']} yosh {talaba_1['kurs']}-kurs")
talaba_1['familyasi']='hayitboyev'
print(talaba_1)
talaba_1['ism']='abror'
print(talaba_1)


telefonlar = {
    'ali':'samsung',
    'hayitboy':'nokia',
    'dilmurod':'redmi',
    'abror':'s21 ultra'
}
print(telefonlar['ali'])

malumotnoma={'ism':'matkarimov olloyorbek','t_yili':1982,'t_joyi':'Hazorasp tumani'}
print(f"Mening otam {malumotnoma['ism'].title()} {malumotnoma['t_yili']}-yil {malumotnoma['t_joyi']} da tugulgan") 

taomlar={'Charosxon':'manti','Hayitboy':'osh','Khurshida':'shorva','Zarifa':'barak','Olloyorbek':'palov'}
print(f"Charosxonning sevimli ovqati {taomlar['Charosxon']}")
print(f"Hayitboyning sevimli ovqati {taomlar['Hayitboy']}")
print(f"Zarifaning sevimli ovqati {taomlar['Zarifa']}")



en_uz={'string':"qo'shtirnoq",'float':"o'nli kasr",'if':'agar','integer':'butun son'}
print(f"String so'zining manosi {en_uz['string']}")
print(f"Float so'zining manosi {en_uz['float']}")
print(f"Integer so'zining manosi {en_uz['integer']}")
print(f"If so'zining manosi {en_uz['if']}")









en_uz={'string':"qo'shtirnoq",'float':"o'nli kasr",'if':'agar','integer':'butun son'}
a = input("Istalgan soz kiriting: ")
tarjima = en_uz.get(a)
if tarjima==None:
    print("bunday soz mavjud emas")
else:
    print(f"{a} so'zi {tarjima} deb tarjima qilinadi")