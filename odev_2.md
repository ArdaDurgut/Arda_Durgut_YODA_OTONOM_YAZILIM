GitHub Lesssons
------------------------------------------------------
cd           Komut satırında çalışmak istediğimiz klasöre girmek için kullanılır.

pwd	         Şu anda bulunduğunuz klasörün/dizinin ne olduğunu gösterir.

git init	 Bulunduğunuz klasörü bir Git deposuna (Repository) dönüştürerek versiyon takibini başlatır.

git status	 Deponuzdaki dosyaların mevcut durumunu (değiştirildi, geçici alana eklendi, kaydedilmedi vb.) gösterir.

git add	     Belirtilen dosyayı bir sonraki (commit) işlemi için geçici alana (Staging Area) ekler.

git add .	 Mevcut dizindeki tüm değiştirilmiş ve yeni dosyaları geçici alana ekler.

git config --global user.name	Kullanıcı adımızı kaydeder.

git config --global user.email	Git'e tüm projeler için e-posta adresinizi kaydeder.

git commit -m "mesaj"	Geçici alandaki değişiklikleri, belirtilen bir mesaj ile kaydeder ve bir commit oluşturur.

git log	Deponun tüm cmomit geçmişini görüntüler.

git diff	Çalışma dizinindeki dosyalar ile en son kaydedilen versiyon arasındaki farkları gösterir.

git diff dosya_adı	Belirtilen dosyadaki değişiklikler ile en son kaydedilen versiyon arasındaki farkları gösterir.

git diff --staged	Geçici alana eklenmiş (staged) olan değişiklikler ile en son kaydedilen versiyon arasındaki farkları gösterir.

git restore dosya_adı	Çalışma dizininde değiştirilmiş olan belirtilen dosyayı, en son kaydedilen (commit edilen) durumuna geri döndürür.

git restore .	Çalışma dizininde değiştirilmiş olan tüm dosyaları en son kaydedilen durumuna geri döndürür.

git reset	Geçici alana eklenen (staged) değişiklikleri çalışma dizinine geri alır (geçici alandan çıkarır).

git config --global --unset user.name	Git'e kaydedilen global kullanıcı adını siler.

git remote add origin LİNK.git	Yerel deponuzu, GitHub'daki uzak depoya (remote) belirtilen bir isimle (genellikle origin) bağlar.

git push LİNK	Yerel commit'lerinizi belirtilen uzak depoya gönderir (paylaşır).

git push -u origin BRANCH	Yerel master (ana) dalınızı, ilk kez olmak üzere, origin adlı uzak depoya gönderir ve gelecekteki push işlemleri için varsayılanı ayarlar.

git clone PROJELİNK	Uzak bir depoda (GitHub vb.) bulunan projenin tam bir kopyasını yerel bilgisayarınıza indirir.

git fetch	Uzak depodaki tüm yeni değişiklikleri (commit'leri ve dalları) yerel deponuza indirir, ancak çalışma dosyalarınızla birleştirmez (merge etmez).

git merge	Farklı bir daldan veya fetch ile çekilen değişiklikleri mevcut çalıştığınız dala birleştirir.

git pull	git fetch (değişiklikleri indir) ve git merge (mevcut dal ile birleştir) işlemlerini tek bir adımda gerçekleştirir.

git branch	Depodaki mevcut tüm dalları (branch) listeler.

git switch	Çalışma alanınızı farklı bir mevcut dala geçirmek için kullanılır.

git switch -c ISIM	Belirtilen isimde yeni bir dal oluşturur ve hemen o dala geçer.

