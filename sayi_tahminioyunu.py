print("1 ile 100 arasında tuttuğum sayıyı bulabilecek misin? ")
#random kütüphanesi ile rastgele sayı çağırabiliriz 
import random
cevap = random.randint(1,100)
tahmin_sayisi = 0
#While ile bir döngü başlattım çünkü bilinemeyen her bir değer için tekrar tahmin yapılması gerekiyor
while True :
    sayi = int(input("Tuttuğum sayı: "))
    #Tutulan sayının bilgisayarın tuttuğu sayı ile eşit olup olmadığını anlamak için koşul atadım
    if(sayi == cevap):
        print("Tebrikler " + str(tahmin_sayisi + 1) + ". denemede cevabı buldunuz")
        break
    elif(sayi < cevap):
        print("Doğru bilemedin tuttuğum sayı daha büyük. Tekrar tahmin etmelisin.")
    elif(sayi > cevap):
        print("Doğru bilemedin tuttuğum sayı daha küçük. Tekrar tahmin etmelisin.")
    tahmin_sayisi = tahmin_sayisi + 1
    #Tahmin sayısını 1 arttırarak kalan tahmini hesapladım ve buna göre oyunun bitmesi için koşul ekledim
    kalan_tahminsayisi = 10 - tahmin_sayisi
    print("Kalan Tahmin Sayınız: " + str(kalan_tahminsayisi))
    if (kalan_tahminsayisi == 0):
            print("Kazanamadınız. Oyun Bitti.")
            break
 


    

    


