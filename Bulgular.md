# Bulgular Ve Analiz Hakkında Bilgi
# Melih Gunaydin - mgunaydin8@gmail.com

**Sayısal Değişkenlerin Betimsel İstatistikleri**
- **Kilo**
  - Frekans = 2064
  - Ortalama = 80.86
  - Standart Sapma = 18.63
  - Minimum = 50
  - İlk çeyreklik (0.25) = 65
  - Medyan (0.50) = 83
  - Üçüncü çeyreklik (0.75) = 96
  - Maksimum = 110

Hastalardan kilosu en düşük olan 50 kilo, en yüksek olan ise 110 kilodur.

- **Boy**
  - Frekans = 2243
  - Ortalama = 174.64
  - Standart Sapma = 16.51
  - Minimum = 145
  - İlk çeyreklik (0.25) = 160
  - Medyan (0.50) = 176
  - Üçüncü çeyreklik (0.75) = 187
  - Maksimum = 203
 
Hastaların en kısası 1.45 en uzunu ise 2.03 cm dir.

**Eksik Değerler**

Eksik değerler aşağıdaki gibidir.

- Kullanici_id                          0
- Cinsiyet                            778
- Dogum_Tarihi                          0
- Uyruk                                 0
- Il                                  227
- Ilac_Adi                              0
- Ilac_Baslangic_Tarihi                 0
- Ilac_Bitis_Tarihi                     0
- Yan_Etki                              0
- Yan_Etki_Bildirim_Tarihi              0
- Alerjilerim                         484
- Kronik Hastaliklarim                392
- Baba Kronik Hastaliklari            156
- Anne Kronik Hastaliklari            217
- Kiz Kardes Kronik Hastaliklari       97
- Erkek Kardes Kronik Hastaliklari    121
- Kan Grubu                           347
- Kilo                                293
- Boy                                 114

**Veri Setinin Boyutu ve Bilgisi**

- 2357 adet gözlem, 19 adet değişken vardır. Bu değişkenlerden 4 tanesi datetime, 2 tanesi float, 1 tanesi integer, 12 tanesi ise object veri tipindedir.

**Kategorik Veriler Hakkında Bilgiler**

- Hastaların, 872 tanesi kadın, 707 tanesi ise erkektir.
- 778 tanesinin cinsiyeti ise bilinmemektedir.
- Bütün hastalar Türk vatandaşıdır.
- Hasta sayısı en çok Adana, en az ise Malatya ve Kayseri şehrine aittir.
- En fazla kullanılan ilaç "chlordiazepoxide-amitriptyline" dır.
- En az kullanılan ilaç ise "lithium carbonate" dir.
- Hastalarda en çok görülen yan etki "Ağızda farklı bir tat" yan etkisidir.
- Hastalarda en az görülen yan etki ise "Deride Morarma" dır.
- Hastaların 484 tanesinin alerjisi yoktur.
- Hastaların 118 tanesinin(en çok) Domatese alerjisi vardır 12 tanesinin(en az) ise kolalı içeceğe alerjisi vardır.
- Hastaların kronik hastalıkları:
  - 'Hipertansiyon': 461,
  - 'Kan Hastaliklari': 383,
  - 'Yok': 392,
  - 'Kalp Hastaliklari': 327,
  - 'Diyabet': 396,
  - 'Diger': 248,
  - 'KOAH': 421,
  - 'Astim': 296,
  - 'Kemik Erimesi': 291,
  - 'Kanser': 273,
  - 'Alzheimer': 343,
  - 'Guatr': 305
bu şekildedir.

- Hastaların Kan grupları ise:
  - AB RH- :       421  
  - NaN     :      347  
  - 0 RH+    :     275  
  - B RH+     :    256  
  - AB RH+    :    250  
  - B RH-     :    233  
  - 0 RH-      :   232  
  - A RH+       :  198  
  - A RH-        : 145  
bu şekildedir.

Aykırı değerler boxplot ile kontrol edilmiştir. Aykırı değerler yoktur. 
- Korelasyonlara bakıldığında ise Boy ve kilo arasındaki korelasyon -0.15'dir. Bu da negatif yönlü zayıf bir korelasyon olduğunu bize söylemektedir.
- Yaş ve kilo arasındaki korelasyon ise 0.03 tür. Bu da pozitif yönlü zayıf bir korelasyon olduğunu bizlere göstermektedir.
- Boy ve yaş arasındaki korelasyon -0.01 dir. Bu de bize negatif yönlü zayıf bir korelasyon olduğunu göstermektedir.
