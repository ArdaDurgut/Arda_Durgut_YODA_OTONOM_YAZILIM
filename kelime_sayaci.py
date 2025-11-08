def metin_istatistikleri():
    metin = input("Lütfen analiz etmek istediğiniz bir cümle veya paragrafı girin: ")
 
    # len() fonksiyonu ile metindeki tüm karakterlerin sayısı hesaplanır.
    toplam_karakter_sayisi = len(metin)
    # Büyük/küçük harf duyarlılığını kaldırmak için metini küçük harfe dönüştürdüm.
    kucuk_metin = metin.lower()

    # Noktalama işaretlerini kaldırmak için metinni temizledim.
    temiz_metin = kucuk_metin.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    
    # split() fonksiyonu ile temizlenmiş metin kelimelere ayrılır.
    kelime_listesi = temiz_metin.split()

    # Oluşturulan listenin uzunluğu bize toplam kelime sayısını veriyor.
    toplam_kelime_sayisi = len(kelime_listesi)

    # Kelimelerin tekrar sayısını tutmak için boş bir sözlük oluşturdum.
    kelime_tekrar = {}

    for kelime in kelime_listesi:
        if kelime in kelime_tekrar:
            kelime_tekrar[kelime] += 1
        else:
            kelime_tekrar[kelime] = 1

    en_uzun_kelime_uzunlugu = 0
    for kelime in kelime_listesi:
        if len(kelime) > en_uzun_kelime_uzunlugu:
            en_uzun_kelime_uzunlugu = len(kelime)

    print("\n--- Metin İstatistikleri ---")
    
    print(f"Toplam Karakter Sayısı (Boşluklar Dahil): {toplam_karakter_sayisi}")
    
    print(f"Toplam Kelime Sayısı: {toplam_kelime_sayisi}")
    
    print(f"En Uzun Kelimenin Uzunluğu: {en_uzun_kelime_uzunlugu} karakter")
    
    print("\n--- Kelime Tekrarları (Büyük/Küçük Harf Fark Etmeksizin) ---")
    
    for kelime, sayi in kelime_tekrar.items():
        print(f"'{kelime}': {sayi} kez")
        
    print("------------------------------------------")

metin_istatistikleri()