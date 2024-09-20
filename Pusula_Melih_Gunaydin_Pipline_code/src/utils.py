import pandas as pd

def summarize_dataframe(df, head_n=5, tail_n=5):
    """Veri çerçevesinin genel özetini sağlar: ilk ve son gözlemler, betimsel istatistikler, boyutlar ve bilgi."""

    print('#' * 30)
    print(f'İlk {head_n} gözlem:')
    print(df.head(head_n))
    print('#' * 30)
    print()

    print('#' * 30)
    print(f'Son {tail_n} gözlem:')
    print(df.tail(tail_n))
    print('#' * 30)
    print()

    print('#' * 30)
    print('Veri çerçevesinin betimsel istatistikleri:')
    print(df.describe().T)
    print('#' * 30)
    print()

    print('#' * 30)
    print('Veri çerçevesinin boyutu:')
    print(df.shape)
    print('#' * 30)
    print()

    print('#' * 30)
    print('Veri çerçevesi hakkında bilgi:')
    print(df.info())
    print('#' * 30)
    print()

    print('#' * 30)
    print('Nan Değerler hakkında bilgi:')
    print(df.isnull().sum())
    print('#' * 30)
    print()

def cat_summary(dataframe, col_name):
    summary_df = pd.DataFrame({col_name: dataframe[col_name].value_counts(dropna=False),
                               "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)})
    print(summary_df)
    print("\n" + "-" * 50 + "\n")
