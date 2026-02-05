import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, numerical_fill="mean",
                 categorical_fill="mode",
                 date_columns=None, 
                 z_threshold=3):
        self.numerical_fill = numerical_fill
        self.categorical_fill = categorical_fill
        self.date_columns = date_columns
        self.z_threshold = z_threshold

    def clean(self, df:pd.DataFrame) -> pd.DataFrame:
        df = self.handle_missing(df)
        df = self.convert_dates(df)
        df = self.remove_outliers(df)

        return df

    def handle_missing(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in df.select_dtypes(include = np.number).columns:
            if self.numerical_fill == 'mean':
                df[col] = df[col].fillna(df[col].mean())
            elif self.numerical_fill == 'median':
                df[col] = df[col].fillna(df[col].median())
            elif isinstance(self.numerical_fill, (int, float)):
                df[col] = df[col].fillna(self.numerical_fill)
        for col in df.select_dtypes(include = "object").columns:
            if self.numerical_fill == 'mode':
                df[col] = df[col].fillna(df[col].mode())
            elif isinstance(self.numerical_fill, str):
                df[col] = df[col].fillna(self.categorical_fill)

        return df
                
    def convert_dates(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in self.date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')
        return df

    def remove_outliers(self, df:pd.DataFrame) -> pd.DataFrame:
        for col in df.select_dtypes(include = np.number).columns:
            mean, std = df[col].mean(), df[col].std()
            z_score = (df[col] - mean)/std

            df = df[z_score.abs() <= self.z_threshold]

        return df

    
if __name__ == '__main__':
    df = pd.read_csv("sample_df.csv")
    cleaner = DataCleaner(date_columns=['Date'])
    clean_df = cleaner.clean(df)
    clean_df.to_csv("cleaned_data.csv", index=False)
    print(clean_df)
