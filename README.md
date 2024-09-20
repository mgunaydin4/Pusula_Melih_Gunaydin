# Pusula_Melih_Gunaydin - Melih Gunaydin - mgunaydin8@gmail.com

Kod Pycharm IDE'sinde yazılmıştır. İlk önce kütüphaneler import edilmiş olup, daha sonrasında ise veri seti yüklenmiştir. (Kütüphanelerin importunda bir problem çıkması halinde "pip" komutunu kullanarak kütüphaneyi projeye dahil etmelisiniz)

## **Bu Case Pipeline Level Code Olarak da yazılmıştır. Pusula_Melih_Gunaydin_Pipline_code dosyasında bu case in Pipeline Level Code hali yazılmıştır.**

"summarize_dataframe" fonksiyonu veri setindeki;

- İlk 5 gözlem
- Son 5 gözlem
- Veri setindeki sayısal değişkenlere ait betimsel istatistikler
- Veri setinin boyutu
- Veri seti hakkında bilgi
- Nan değerler hakkında bilgi

içermektedir. 

Daha sonrasında ise Kategorik değişkenler hakkında bilgi sahibi olmak için "cat_summary" fonksiyonu yazılmıştır. Bu fonksiyonda ise;

- Nan değerler silinmemiş olup, kategorik değişkenlerdeki değerlerin frekansları ve yüzdeleri gösterilmektedir.

Daha sonra ise elimizde "dogum_tarihi" isimli değişken kullanılarak analizin yapıldığı tarih(18/9/2024) dogum tarihinden çıkarılarak yeni bir "Yaş" değişkeni oluşturulmuştur.


Yine aynı şekilde elimizde ilaç bitiş ve ilac baslangic değişkenleri vardı. Bu değişkenleri kullanarak hastanın ilacı kaç gün kullandığı hesaplanmış ve "Ilac_kullanim_suresi(gun)" isimli değişken oluşturulmuştur.

Ve yine aynı şekilde yan etkinin ilaç kullanılmaya başlandıktan kaç gün sonra ortaya çıktığını hesaplamak için yan etki tarihinden ilaç başlangıç tarihi çıkarılmıştır.

Daha sonrasında ise tarih tipine sahip olan değişkenler ve kullanici_id gereksiz olduğu için silinmiştir.

## Verilerin Görselleştirilmesi

Veriler görselleştirilirken 2 kütüphaneden yararlanılmıştır.

- plotly.express
- matplotlib

Plotly.express kullanımında fonksiyon yazılmıştır ve switch - case yapısı kullanılmıştır. Varsayılan olarak matplotlib kütüphanesi kullanıldığı için 232. satırdaki;

- #visualize_data(df, 'Boy')  # Grafik türünü buraya belirtin. (Grafik çıktısı alındıktan sonra control+c ile port u kapatın!)

kod yorum satırı durumundadır. Yorum satırını kaldırarak kullanabilirsiniz. Görselleştirme web sayfasında açılacaktır. Görselleştirmeyi inceledikten sonra python consoledan portu,

- windows için : ctrl + c
- mac için : control + c

ile kapatmalısınız.

Matplotlib kütüphanesinde ise local olarak çalışacağınızdan bir problem olmayacaktır. Switch - case yapısındaki değişkenlerden istediğiniz değişkeni görselleştirebilirsiniz

Örnek

- visualize_data(df, 'Boy')

Boy değişkenini görselleştirir.

Daha sonra ise bazı groupby işlemleri yapılmıştır.

## Eksik Verilerin Analizi

**"handle_missing_values" fonksiyonu ile,**

- Uyruk değişkeni kaldırılmıştır
- **"Alerjilerim", "Kronik Hastaliklarim", "Baba Kronik Hastaliklari", "Anne Kronik Hastaliklari", "Kiz Kardes Kronik Hastaliklari", "Erkek Kardes Kronik Hastaliklari"** değişkenlerinin Nan değerleri "Yok" değeri ile doldurulmuştur.
- Sayısal değişkenler "Medyan" ile doldurulmuştur.
- **"Kan Grubu", "Il", "Cinsiyet"** değişkenleri ise "Bilinmiyor" değeri ile doldurulmuştur.

Daha sonrasında ise Min-Max Scaler yöntemi ile sayısal veriler standartlaştırılmış, kategorik değişkenler ise label_encoding yöntemi ile sayısal verilere dönüştürülmüştür.

En sonunda ise model için hazırlanan veri **df_encoded** isimli değişkene atanmıştır.


