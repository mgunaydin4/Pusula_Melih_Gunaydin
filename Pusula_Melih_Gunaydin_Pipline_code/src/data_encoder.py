from sklearn.preprocessing import MinMaxScaler, LabelEncoder

class DataEncoder(object):
    def __init__(self, df):
        self.df = df

    def encoder(self):
        self._standardize_numerical_data()
        self._encode_categorical_data()
        return self.df

    def _standardize_numerical_data(self):
        numerical_columns = ['Kilo', 'Boy', 'Yaş', 'Ilac_kullanim_suresi(gun)', 'Yan_etki_ne_zaman_basladi']
        scaler = MinMaxScaler()
        self.df[numerical_columns] = scaler.fit_transform(self.df[numerical_columns])


    def _encode_categorical_data(self):
        categorical_columns = self.df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            le = LabelEncoder()
            self.df[f'{column}_encoded'] = le.fit_transform(self.df[column])
        self.df = self.df.drop(columns=categorical_columns)

