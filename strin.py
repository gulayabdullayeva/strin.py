# string  ve ya str tip
# Gulay = "Gulay"
# suraname = input("soyadinizi daxil edin: ")
#print (name , surame)
#print (name[0])
#print (name[1])
#print (name[2])
#print (name[3])
#print (name[4])

#print (name[-1])
#print (name[-2])
#print (name[-3])
#print (name[-4])
#print (name[-5])
#print  (len(Name))
#slicing --> [baslanginc :son : step ]
#text = "python programing language"

#print (text[0:5])
#print (text[:6])

#print (text[::]) #print (text) ile eynidir
#print (text[::-1])
#print (text[::2])
#print (text[7::18])
#print (text[19::26])
#print (text[7::18])
#print (text[19::])
#sting metodu


print (len(name))


#1. upper() metodu metni boyuk heriflere cevirir
from pydoc import text


print("salam".upper())

# 2. lover() metodu metni kicik heriflere cevirir
print("SALAM".lower())

# 3. title() metodu metnin her sozunun ilk herifini boyuk herife cevirir
print("salam, men gulay".title())

# 4. strip() metodu metnin basinda ve sonunda olan bosluqlari silir
print("Gulay")
print("Gulay".strip())

# 5. count() metodu metnin icinde verilmis simvolun nece defe oldugunu yoxlayir
print ( text. count("a"))
print (text. count ("p"))

#6. replace() metodu metnin icinde verilmis simvolu diger simvolla evezleyir
print("2,9".replace(",", "."))
print("2.9".replace("a", "A"))

#  7.isalpha yalniz herifleri yoxlaryir
ad = input("Adinizi daxil edin: ")
print (ad.isalpha())

# 8. isupper yalniz boyuk herifleri yoxlayir
print (ad.isupper())
print (ad.isupper())

#. 9. islower yalniz kicik herifleri yoxlayir
print (ad.islower())
# print (ad.islower())

#10.startswith() verilmis metinle baslayib baslamadigini yoxlayir
metin = "Salam, men Gulay"
print (metin.startswith("Salam"))
print (metin.startswith("men"))

#11. endswith() verilmis metinle bitib-bitmediyini yoxlayir
metin1 = "Salam, men Gulay"
print (metin1.endswith("Gulay"))
print (metin1.endswith("men"))

#12. join() metodu verilmis siyahidaki elementleri birlesdirir
siyahi = ["Salam", "men", "Gulay"]
cumle = " ".join(siyahi)
print(cumle)
