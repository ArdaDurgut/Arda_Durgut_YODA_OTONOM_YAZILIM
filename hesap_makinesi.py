#While döngüsü ile 0'a bölünememe durumuna karşı tekrar işlem yapabilmeyi sağladım
while True:
    ilkSayi = int(input("İlk Sayıyı Giriniz: "))
    ikinciSayi = int(input("İkinci Sayıyı Giriniz: "))
    islem = input("""Yapmak İstediğiniz İşlemi Giriniz: 
(Toplama: +, Çıkarma: -, Çarpma: *, Bölme: /)
""")
#Kullanıcıdan iki sayı ve bir işlem değeri aldım
#Seçilen işleme göre matematik işlemini gerçekleştirebilmek için koşul ekledim
    if islem == "+":
        print("Sonuç: " + str(ilkSayi + ikinciSayi))
        #Sonucu bulduktan sonra tekrar etmemesi için döngüyü kırdım
        break

    elif islem == "-":
        print("Sonuç: " + str(ilkSayi - ikinciSayi))
        #Sonucu bulduktan sonra tekrar etmemesi için döngüyü kırdım
        break

    elif islem == "*":
        print("Sonuç: " + str(ilkSayi * ikinciSayi))
        #Sonucu bulduktan sonra tekrar etmemesi için döngüyü kırdım
        break

    elif islem == "/":
        # Sıfıra bölme hatasını kontrol etmek için koşul ekledim.
        if ikinciSayi != 0:
            print("Sonuç: " + str(ilkSayi / ikinciSayi))
            #Seçilen sayı sıfır olmadığı için döngünün tekrar etmemesi için döngüyü kırdım
            break
        else:
            print("Ben bi sayıyı sıfıra bölemiyorum. Valla sen bölebiliyorsan bi dene :D ")
            #Döngü devam etmesi için burayı break etmedim

    else:
        print("Hata: Geçersiz bir işlem girdiniz. Lütfen (+, -, *, /) işlemlerinden birini kullanın.")
        #Sıfırda olduğu gibi girilen işlemin doğruluğu için burayı da break etmedim