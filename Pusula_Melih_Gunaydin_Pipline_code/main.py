import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

import pandas as pd
from data_loader import DataLoader
from data_preprocessor import DataPreprocessor
from data_visualizer import DataVisualizer
from data_analyzer import DataAnalyzer
from src.data_encoder import DataEncoder
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar.
pd.set_option('display.expand_frame_repr', False)

def main():
    # Load data
    data_loader = DataLoader("data/side_effect_data 1.xlsx")
    df = data_loader.load_data()

    # Preprocess data
    preprocessor = DataPreprocessor(df)
    df_preprocessed = preprocessor.preprocess()

    # Visualize data
    visualizer = DataVisualizer(df_preprocessed)
    visualizer.visualize_all()

    # Analyze data
    analyzer = DataAnalyzer(df_preprocessed)
    analyzer.analyze()

    # Encoder Data
    encoder = DataEncoder(df_preprocessed)
    df_encoded = encoder.encoder()

    print("########################################## Encode Edilmiş Veri: Model için Hazırlanan Veri ##########################################")
    print(df_encoded)

if __name__ == "__main__":
    main()
