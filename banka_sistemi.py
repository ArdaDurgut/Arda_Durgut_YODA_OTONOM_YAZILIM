class Hesap:
    # Hesap sınıfının başlatıcısı (constructor)
    def __init__(self, ad_soyad, hesap_no, baslangic_bakiye=0):
        # Hesap sahibinin bilgileri
        self.ad_soyad = ad_soyad
        self.hesap_no = hesap_no
        self.bakiye = baslangic_bakiye

    # Para yatırma fonksiyonu
    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"\n{miktar} TL hesabınıza yatırıldı.")
            self.bakiye_goruntule()
        else:
            print("\nGeçersiz miktar. Yatırılan miktar pozitif olmalıdır.")

    # Para çekme fonksiyonu
    def para_cek(self, miktar):
        if miktar > 0:
            if self.bakiye >= miktar:
                self.bakiye -= miktar
                print(f"\n{miktar} TL hesabınızdan çekildi.")
                self.bakiye_goruntule()
            else:
                print("\nYetersiz bakiye! İşlem gerçekleştirilemedi.")
        else:
            print("\nGeçersiz miktar. Çekilen miktar pozitif olmalıdır.")

    # Bakiye görüntüleme fonksiyonu
    def bakiye_goruntule(self):
        print(f"\n--- Hesap Bilgileri ---")
        print(f"Hesap Sahibi: {self.ad_soyad}")
        print(f"Hesap No: {self.hesap_no}")
        print(f"Güncel Bakiye: {self.bakiye} TL")
        print(f"------------------------")


def main():
    print("### Yeni Hesap Oluşturma ###")

    # Kullanıcıdan hesap bilgilerini al
    sahip_adi = input("Hesap Sahibinin Adı Soyadı: ")
    hesap_numarasi = input("Hesap Numarası: ")
    
    # Başlangıç bakiyesi için basit bir kontrol
    while True:
        try:
            bakiye_miktari = float(input("Başlangıç Bakiyesi (TL): "))
            if bakiye_miktari >= 0:
                break
            else:
                print("Başlangıç bakiyesi negatif olamaz. Lütfen tekrar girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")


    banka_hesabi = Hesap(sahip_adi, hesap_numarasi, bakiye_miktari)
    print("\nHesap Başarıyla Oluşturuldu!")
    banka_hesabi.bakiye_goruntule()

    while True:
        print("\n### Hesap Yönetimi Menüsü ###")
        print("1. Para Yatır")
        print("2. Para Çek")
        print("3. Bakiye Görüntüle")
        print("4. Çıkış")

        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ")

        if secim == '1':
            try:
                miktar = float(input("Yatırmak istediğiniz miktarı girin (TL): "))
                banka_hesabi.para_yatir(miktar)
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")

        elif secim == '2':
            try:
                miktar = float(input("Çekmek istediğiniz miktarı girin (TL): "))
                banka_hesabi.para_cek(miktar)
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")

        elif secim == '3':
            banka_hesabi.bakiye_goruntule()

        elif secim == '4':
            print("\nProgramdan çıkılıyor. Bizi tercih ettiğiniz için teşekkürler!")
            break

        else:
            print("\nGeçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")

if __name__ == "__main__":
    main()