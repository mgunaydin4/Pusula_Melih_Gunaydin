import pandas as pd
import numpy as np
import datetime as dt

class DataPreprocessor:
    def __init__(self, df):
        self.df = df.copy()

    def preprocess(self):
        self._calculate_age()
        self._calculate_drug_usage_duration()
        self._calculate_side_effect_start()
        self._remove_unnecessary_columns()
        self._handle_missing_values()
        return self.df

    def _calculate_age(self):
        today_date = dt.datetime(2024, 9, 18)
        self.df["Yaş"] = (today_date - self.df["Dogum_Tarihi"]).dt.days // 365
        self.df.drop("Dogum_Tarihi", inplace=True, axis=1)

    def _calculate_drug_usage_duration(self):
        self.df["Ilac_kullanim_suresi(gun)"] = (self.df["Ilac_Bitis_Tarihi"] - self.df["Ilac_Baslangic_Tarihi"]).dt.days

    def _calculate_side_effect_start(self):
        self.df["Yan_etki_ne_zaman_basladi"] = (self.df["Yan_Etki_Bildirim_Tarihi"] - self.df["Ilac_Baslangic_Tarihi"]).dt.days

    def _remove_unnecessary_columns(self):
        self.df.drop(columns=["Ilac_Bitis_Tarihi", "Ilac_Baslangic_Tarihi", "Yan_Etki_Bildirim_Tarihi", "Kullanici_id"], inplace=True, axis=1)

    def _handle_missing_values(self):
        if 'Uyruk' in self.df.columns:
            self.df.drop(columns=["Uyruk"], axis=1, inplace=True)

        categorical_columns = ["Alerjilerim", "Kronik Hastaliklarim", "Baba Kronik Hastaliklari",
                               "Anne Kronik Hastaliklari", "Kiz Kardes Kronik Hastaliklari",
                               "Erkek Kardes Kronik Hastaliklari"]
        self.df[categorical_columns] = self.df[categorical_columns].fillna("Yok")

        numerical_columns = ['Kilo', 'Boy']
        for col in numerical_columns:
            if col in self.df.columns:
                self.df[col].fillna(self.df[col].median(), inplace=True)

        other_columns = ['Kan Grubu', 'Il', 'Cinsiyet']
        for col in other_columns:
            if col in self.df.columns:
                self.df[col].fillna('Bilinmiyor', inplace=True)


