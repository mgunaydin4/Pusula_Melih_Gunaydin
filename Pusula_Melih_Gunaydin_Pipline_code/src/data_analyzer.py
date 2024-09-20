class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        self.drug_gender_analysis()
        self.gender_age_analysis()
        self.blood_age_weight_analysis()

    def drug_gender_analysis(self):
        result = self.df.groupby(["Ilac_Adi", "Cinsiyet"]).agg({
            'Yaş': "mean",
            "Ilac_kullanim_suresi(gun)": "mean",
            "Yan_etki_ne_zaman_basladi": "mean"
        })
        print("İlaç - Cinsiyet Kırılımında Ortalama Yaş, Ortalama Ilac Kullanim Suresi ve Ortalama Yan Etki Süresi:")
        print(result)
        print("\n")

    def gender_age_analysis(self):
        result = self.df.groupby(["Cinsiyet", "Yaş"]).agg({
            "Ilac_kullanim_suresi(gun)": "mean",
            "Yan_etki_ne_zaman_basladi": "mean"
        })
        print("Cinsiyet - Yaş Kırılımında Ortalama Ilac Kullanim Suresi ve Ortalama Yan Etki Süresi:")
        print(result)
        print("\n")

    def blood_age_weight_analysis(self):
        result = self.df.groupby(["Kan Grubu", "Yaş", "Kilo"]).agg({
            "Ilac_kullanim_suresi(gun)": "mean",
            "Yan_etki_ne_zaman_basladi": "mean"
        })
        print("Kan Grubu - Yaş - Kilo kırılımında Ortalama Ilac Kullanim Suresi ve Ortalama Yan Etki Süresi:")
        print(result)
        print("\n")
