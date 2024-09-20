import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def visualize_all(self):
        self.plot_pie_chart('Cinsiyet', 'Cinsiyet Dağılımı')
        self.plot_histogram('Yaş', 'Yaş Dağılımı')
        self.plot_pie_chart('Il', 'İl Dağılımı')
        self.plot_bar_chart('Ilac_Adi', 'İlaçların Dağılımı')
        self.plot_pie_chart('Yan_Etki', 'Yan Etki Dağılımı')
        self.plot_bar_chart('Kronik Hastaliklarim', 'Kronik Hastalık Dağılımı')
        self.plot_histogram('Kilo', 'Kilo Dağılımı')
        self.plot_histogram('Boy', 'Boy Dağılımı')
        self.plot_pie_chart('Alerjilerim', 'Alerji Dağılımı')
        self.plot_correlation_heatmap()

    def plot_pie_chart(self, column, title):
        plt.figure(figsize=(8, 6))
        self.df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(title)
        plt.axis('equal')
        plt.show()

    def plot_bar_chart(self, column, title):
        plt.figure(figsize=(10, 6))
        self.df[column].value_counts().plot(kind='bar')
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_histogram(self, column, title):
        plt.figure(figsize=(10, 6))
        plt.hist(self.df[column], bins=30, edgecolor='black')
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def plot_correlation_heatmap(self):
        corr_matrix = self.df[["Boy", "Kilo", "Yaş", "Ilac_kullanim_suresi(gun)", "Yan_etki_ne_zaman_basladi"]].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Değişkenler Arası Korelasyon Isı Haritası")
        plt.show()
