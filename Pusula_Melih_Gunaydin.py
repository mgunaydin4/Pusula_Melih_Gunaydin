# Kütüphanelerin import edilmesi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import datetime as dt
from collections import Counter
import http.server
import socketserver
import webbrowser
import threading
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
pd.set_option('display.max_columns', None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


# DataFrame import edilmesi
df_ = pd.read_excel("side_effect_data 1.xlsx")
df = df_.copy()

# Veriye İlk Bakış
def summarize_dataframe(df, head_n=5, tail_n=5):
    """Veri çerçevesinin genel özetini sağlar: ilk ve son gözlemler, betimsel istatistikler, boyutlar ve bilgi."""

    # ---------------------------
    # İlk n gözlem
    # ---------------------------
    print('#' * 30)
    print(f'İlk {head_n} gözlem:')
    print(df.head(head_n))
    print('#' * 30)
    print()  # Satır sonu

    # ---------------------------
    # Son n gözlem
    # ---------------------------
    print('#' * 30)
    print(f'Son {tail_n} gözlem:')
    print(df.tail(tail_n))
    print('#' * 30)
    print()  # Satır sonu

    # ---------------------------
    # Betimsel istatistikler
    # ---------------------------
    print('#' * 30)
    print('Veri çerçevesinin betimsel istatistikleri:')
    print(df.describe().T)
    print('#' * 30)
    print()  # Satır sonu

    # ---------------------------
    # Veri çerçevesinin boyutu
    # ---------------------------
    print('#' * 30)
    print('Veri çerçevesinin boyutu:')
    print(df.shape)
    print('#' * 30)
    print()  # Satır sonu

    # ---------------------------
    # Veri çerçevesi hakkında bilgi
    # ---------------------------
    print('#' * 30)
    print('Veri çerçevesi hakkında bilgi:')
    print(df.info())
    print('#' * 30)
    print()  # Satır sonu

    # ---------------------------
    # Nan değerler hakkında bilgi
    # ---------------------------
    print('#' * 30)
    print('Nan Değerler hakkında bilgi:')
    print(df.isnull().sum())
    print('#' * 30)
    print()  # Satır sonu
summarize_dataframe(df)


# Kategorik değişkenlerin analizi
def cat_summary(dataframe, col_name):
    # Kategorik değişkenin frekans ve yüzde özetini çıkarır
    summary_df = pd.DataFrame({col_name: dataframe[col_name].value_counts(dropna=False),
                               "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)})
    print(summary_df)
    print("\n" + "-" * 50 + "\n")


for col in df.select_dtypes(include=['object']).columns:
    cat_summary(df, col)

# Yaşı hesaplamak için yeni bir değişken oluşturma ve Dogum_Tarihi isimli değişkeni veriden kaldırma
today_date = dt.datetime(2024, 9, 18)
df["Yaş"] = (today_date - df["Dogum_Tarihi"]).dt.days // 365
df.drop("Dogum_Tarihi", inplace=True, axis=1)
df.head()

# İlac kullanım süresini hesaplama
df["Ilac_kullanim_suresi(gun)"] = (df["Ilac_Bitis_Tarihi"] - df["Ilac_Baslangic_Tarihi"]).dt.days
df.head()

# Yan etki ilaç kullanmaya başlandıktan kaç gün sonra başladı ? (Yan_Etki_Bildirim_Tarihi - Ilac_Baslangic_Tarihi)
df["Yan_etki_ne_zaman_basladi"] = (df["Yan_Etki_Bildirim_Tarihi"] - df["Ilac_Baslangic_Tarihi"]).dt.days

# Gereksiz değişkenlerin Silinmesi
df.drop(columns=["Ilac_Bitis_Tarihi", "Ilac_Baslangic_Tarihi", "Yan_Etki_Bildirim_Tarihi", "Kullanici_id"], inplace=True, axis=1)
df.head()

# Eksik Verilerin Doldurulması
def handle_missing_values(df):
    """
    Eksik değerlerle ilgili işlemleri yapan fonksiyon.

    Parametreler:
    df (pd.DataFrame): Eksik değerleri olan veri çerçevesi.

    Döndürür:
    pd.DataFrame: Eksik değerler doldurulmuş veri çerçevesi.
    """

    # Uyruk değişkenini veri setinden kaldır
    if 'Uyruk' in df.columns:
        df.drop(columns=["Uyruk"], axis=1, inplace=True)

    # Kategorik değişkenlerde eksik değerleri "Yok" ile doldur
    sutunlar = ["Alerjilerim", "Kronik Hastaliklarim", "Baba Kronik Hastaliklari",
                "Anne Kronik Hastaliklari", "Kiz Kardes Kronik Hastaliklari",
                "Erkek Kardes Kronik Hastaliklari"]

    df[sutunlar] = df[sutunlar].fillna("Yok")

    # Medyan hesaplama ve eksik değerleri medyan ile doldurma
    if 'Kilo' in df.columns:
        medyan_kilo = df['Kilo'].median()
        df['Kilo'].fillna(medyan_kilo, inplace=True)

    if 'Boy' in df.columns:
        medyan_boy = df['Boy'].median()
        df['Boy'].fillna(medyan_boy, inplace=True)

    # Eksik değerleri "Bilinmiyor" ile doldurma
    if 'Kan Grubu' in df.columns:
        df['Kan Grubu'].fillna('Bilinmiyor', inplace=True)

    if 'Il' in df.columns:
        df['Il'].fillna('Bilinmiyor', inplace=True)

    if 'Cinsiyet' in df.columns:
        df['Cinsiyet'].fillna('Bilinmiyor', inplace=True)

    return df

handle_missing_values(df)

def outlier_thresholds(dataframe, col_name, q1=0.05, q3=0.95):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


# Analiz fonksiyonu
def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False

def replace_with_thresholds(dataframe, variable, q1=0.05, q3=0.95):
    low_limit, up_limit = outlier_thresholds(dataframe, variable, q1=0.05, q3=0.95)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


# Aykırı Değer Analizi ve Baskılama İşlemi

num_cols = [i for i in df.columns if df.dtypes[i] in ["int64", "float64"]]

for col in num_cols:
    print(col, check_outlier(df, col))
    if check_outlier(df, col):
        replace_with_thresholds(df, col)





############################################## Verilerin Görselleştirilmesi ##############################################

############################################## Plotly Express ##############################################

# Başlangıç port numarası
START_PORT = 8000
PORT_INCREMENT = 1

def get_next_port():
    """Bir sonraki port numarasını döndür."""
    global START_PORT
    port = START_PORT
    START_PORT += PORT_INCREMENT
    return port

def save_and_show_plot(fig, filename='grafik.html'):
    """Grafiği HTML dosyasına kaydet ve basit bir HTTP sunucusu ile göster."""
    fig.write_html(filename)

    # Port numarasını al
    PORT = get_next_port()
    Handler = http.server.SimpleHTTPRequestHandler

    def run_server():
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Sunucu {PORT} portunda çalışıyor...")
            webbrowser.open(f'http://localhost:{PORT}/{filename}')
            httpd.serve_forever()

    # Sunucuyu ayrı bir thread'de çalıştır
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    server_thread.join()  # Sunucu kapanana kadar bekleyin

def plot_pie_chart(values, names, title):
    """Pasta grafiği çizen fonksiyon."""
    fig = px.pie(values=values, names=names, title=title)
    save_and_show_plot(fig, 'pie_chart.html')

def plot_bar_chart(x, y, title, x_title, y_title):
    """Çubuk grafiği çizen fonksiyon."""
    fig = px.bar(x=x, y=y, text_auto='.2s', title=title)
    fig.update_layout(xaxis_title=x_title, yaxis_title=y_title)
    save_and_show_plot(fig, 'bar_chart.html')

def plot_histogram(x, title):
    """Histogram çizen fonksiyon."""
    fig = px.histogram(x=x, title=title)
    save_and_show_plot(fig, 'histogram.html')

def visualize_data(df, chart_type):
    """Veri setine göre uygun grafiği çizen ana fonksiyon."""
    switch = {

        ############################################## Cinsiyet Değişkeni Görselleştirme ##############################################
        'Cinsiyet': lambda: plot_pie_chart(df['Cinsiyet'].value_counts().values,
                                           df['Cinsiyet'].value_counts().index,
                                           'Cinsiyet Dağılımı  )'),

        ############################################## Yaş Değişkeni Görselleştirme ##############################################
        'Yaş': lambda: plot_histogram(df['Yaş'], 'Yaş Dağılımı  )'),

        ############################################## İl Değişkeni Görselleştirme ##############################################
        'İl': lambda: plot_pie_chart(df['Il'].value_counts().values,
                                     df['Il'].value_counts().index,
                                     'İl Dağılımı  )'),

        ############################################## İlaç Değişkeni Görselleştirme ##############################################
        'İlaç': lambda: plot_bar_chart(df['Ilac_Adi'].value_counts().index,
                                       df['Ilac_Adi'].value_counts().values,
                                       'İlaçların Dağılımı',
                                       'İlaç Adı',
                                       'Adet'),

        ############################################## Yan Etki Değişkeni Görselleştirme ##############################################
        'Yan Etki': lambda: plot_pie_chart(df['Yan_Etki'].value_counts().values,
                                           df['Yan_Etki'].value_counts().index,
                                           'Yan Etki Dağılımı  )'),

        ############################################## Kronik Hastalık Değişkeni Görselleştirme ##############################################

        'Kronik Hastalık': lambda: plot_bar_chart(df['Kronik Hastaliklarim'].value_counts().index,
                                                 df['Kronik Hastaliklarim'].value_counts().values,
                                                 'Kronik Hastalık Dağılımı',
                                                 'Kronik Hastalık',
                                                 'Adet'),

        ############################################## Kronik Hastalık (Unique değerler ile ayrılmış) Değişkeni Görselleştirme ##############################################

        'Kronik Hastalık Ayrı': lambda: plot_pie_chart(pd.DataFrame(Counter(
            [item for sublist in df['Kronik Hastaliklarim'].fillna("Yok").str.split(", ")
             for item in sublist]).items(),
            columns=['Hastalik', 'Frekans']).sort_values('Frekans', ascending=False)['Frekans'].values,
            pd.DataFrame(Counter(
            [item for sublist in df['Kronik Hastaliklarim'].fillna("Yok").str.split(", ")
             for item in sublist]).items(),
            columns=['Hastalik', 'Frekans']).sort_values('Frekans', ascending=False)['Hastalik'].values,
            'Kronik Hastalıkların Dağılımı'),

        ############################################## Kilo Değişkeni Görselleştirme ##############################################
        'Kilo': lambda: plot_histogram(df['Kilo'], 'Kilo Dağılımı  )'),

        ############################################## Boy Değişkeni Görselleştirme ##############################################
        'Boy': lambda: plot_histogram(df['Boy'], 'Boy Dağılımı  )'),

        ############################################## Alerji Değişkeni Görselleştirme ##############################################
        'Alerji': lambda: plot_pie_chart(df['Alerjilerim'].value_counts().values,
                                         df['Alerjilerim'].value_counts().index,
                                         'Alerji Dağılımı  )'),


    }

    func = switch.get(chart_type)
    if func:
        func()
    else:
        print("Geçersiz grafik türü!")

# Örnek kullanım:
#visualize_data(df, 'Cinsiyet')  # Grafik türünü buraya belirtin. (Grafik çıktısı alındıktan sonra control+c ile port u kapatın!)


############################################## Matplotlib ##############################################
def plot_pie_chart(values, names, title):
    """Pasta grafiği çizen fonksiyon."""
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=names, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')  # Eşit eksen oranı
    plt.show()

def plot_bar_chart(x, y, title, x_title, y_title):
    """Çubuk grafiği çizen fonksiyon."""
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='skyblue')
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  # Etiketlerin kesilmesini önler
    plt.show()

def plot_histogram(x, title):
    """Histogram çizen fonksiyon."""
    plt.figure(figsize=(10, 6))
    plt.hist(x, bins=30, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Değerler')
    plt.ylabel('Frekans')
    plt.tight_layout()
    plt.show()

def visualize_data(df, chart_type):
    """Veri setine göre uygun grafiği çizen ana fonksiyon."""
    switch = {

        'Cinsiyet': lambda: plot_pie_chart(df['Cinsiyet'].value_counts().values,
                                           df['Cinsiyet'].value_counts().index,
                                           'Cinsiyet Dağılımı  )'),

        'Yaş': lambda: plot_histogram(df['Yaş'], 'Yaş Dağılımı  )'),

        'İl': lambda: plot_pie_chart(df['Il'].value_counts().values,
                                     df['Il'].value_counts().index,
                                     'İl Dağılımı  )'),

        'İlaç': lambda: plot_bar_chart(df['Ilac_Adi'].value_counts().index,
                                       df['Ilac_Adi'].value_counts().values,
                                       'İlaçların Dağılımı',
                                       'İlaç Adı',
                                       'Adet'),

        'Yan Etki': lambda: plot_pie_chart(df['Yan_Etki'].value_counts().values,
                                           df['Yan_Etki'].value_counts().index,
                                           'Yan Etki Dağılımı  )'),

        'Kronik Hastalık': lambda: plot_bar_chart(df['Kronik Hastaliklarim'].value_counts().index,
                                                 df['Kronik Hastaliklarim'].value_counts().values,
                                                 'Kronik Hastalık Dağılımı',
                                                 'Kronik Hastalık',
                                                 'Adet'),

        'Kronik Hastalık Ayrı': lambda: plot_pie_chart(pd.DataFrame(Counter(
            [item for sublist in df['Kronik Hastaliklarim'].fillna("Yok").str.split(", ")
             for item in sublist]).items(),
            columns=['Hastalik', 'Frekans']).sort_values('Frekans', ascending=False)['Frekans'].values,
            pd.DataFrame(Counter(
            [item for sublist in df['Kronik Hastaliklarim'].fillna("Yok").str.split(", ")
             for item in sublist]).items(),
            columns=['Hastalik', 'Frekans']).sort_values('Frekans', ascending=False)['Hastalik'].values,
            'Kronik Hastalıkların Dağılımı'),

        'Kilo': lambda: plot_histogram(df['Kilo'], 'Kilo Dağılımı  )'),

        'Boy': lambda: plot_histogram(df['Boy'], 'Boy Dağılımı  )'),

        'Alerji': lambda: plot_pie_chart(df['Alerjilerim'].value_counts().values,
                                         df['Alerjilerim'].value_counts().index,
                                         'Alerji Dağılımı  )')
    }

    func = switch.get(chart_type)
    if func:
        func()
    else:
        print("Geçersiz grafik türü!")

# Örnek kullanım:
visualize_data(df, 'Cinsiyet')  # Grafik türünü buraya belirtin.

# İlaç - Cinsiyet Kırılımında Ortalama Yaş, Ortalama Ilac Kullanim Suresi ve Ortalama Yan Etki Süresi
df.groupby(["Ilac_Adi", "Cinsiyet"]).agg({
    'Yaş': "mean",
    "Ilac_kullanim_suresi(gun)": "mean",
    "Yan_etki_ne_zaman_basladi": "mean"
})

# Cinsiyet - Yaş Kırılımında Ortalama Ilac Kullanim Suresi ve Ortalama Yan Etki Süresi
df.groupby(["Cinsiyet", "Yaş"]).agg({
    "Ilac_kullanim_suresi(gun)": "mean",
    "Yan_etki_ne_zaman_basladi": "mean"
})

# Kan Grubu - Yaş - Kilo kırılımında  Ortalama Ilac Kullanim Suresi ve Ortalama Yan Etki Süresi
df.groupby(["Kan Grubu", "Yaş", "Kilo"]).agg({
    "Ilac_kullanim_suresi(gun)": "mean",
    "Yan_etki_ne_zaman_basladi": "mean"
})


# Korelasyon Hesaplama
corr_matrix = df[["Boy", "Kilo", "Yaş", "Ilac_kullanim_suresi(gun)", "Yan_etki_ne_zaman_basladi"]].corr()

# Isı haritasını çiz
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Değişkenler Arası Korelasyon Isı Haritası")
plt.show()


df.head()
df.isnull().sum()

# Sayısal Verileri Standartlaştırma
sayisal_degiskenler = ['Kilo', 'Boy', 'Yaş', 'Ilac_kullanim_suresi(gun)', 'Yan_etki_ne_zaman_basladi']

# MinMaxScaler'ı oluştur
scaler = MinMaxScaler()

# Sayısal verileri ölçeklendirme
df[sayisal_degiskenler] = scaler.fit_transform(df[sayisal_degiskenler])

df.head()

# Kategorik Değişkenleri Sayısal Değişkene Çevirme

# Label Encoder nesnesi oluşturma
label_encoders = {}

# Kategorik sütunları döngü ile dönüştürme
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[f'{column}_encoded'] = le.fit_transform(df[column])
    label_encoders[column] = le

df_encoded = df.drop(columns=df.select_dtypes(include=['object']).columns)

df_encoded.head()
