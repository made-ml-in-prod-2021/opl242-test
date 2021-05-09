import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
# from sklearn.base import BaseEstimator, ClassifierMixin

# Нужен трансформер

# -----------------------------------------------------------------------------
# class ToCategory():  # BaseEstimator, ClassifierMixin
#     def __init__(self, col):
#         self.col = col

#     def fit(self, col):
#         self.col = col


#     def transform(self):
#         return pd.Categorical(self.col).cat.codes


# -----------------------------------------------------------------------------
# class CleanColor(): 
#     def __init__(self, col):
#         self.col = col

#     def fit(self, col):
#         self.col = col


# -----------------------------------------------------------------------------
def rename_columns(df):
    rename_cols = {
        'Temperature (K)': 'temperature',
        'Luminosity(L/Lo)': 'luminosity',
        'Radius(R/Ro)': 'radius',
        'Absolute magnitude(Mv)': 'magnitude',
        'Star type': 'type',
        'Star color': 'color',
        'Spectral Class': 'class'
    }

    df = df.rename(columns=rename_cols)
    return df


# -----------------------------------------------------------------------------
def clean_color(col):
    return (
        col.str.lower().str.replace(" ", "")
        .str.replace("-", "")
        .str.replace("yellowishwhite", "yellowwhite")
        .str.replace("whiteyellow", "yellowwhite")
        .str.replace("whitish", "white")
        .str.replace("orangered", "orange")
        .str.replace("paleyelloworange", "orange")
    )


# -----------------------------------------------------------------------------
def build_categorical_pipeline() -> Pipeline:
    categorical_pipeline = Pipeline(
        [
            ("le", LabelEncoder()),
        ]
    )
    return categorical_pipeline


# -----------------------------------------------------------------------------
def process_raw_dataset(df):

    df = rename_columns(df)
    df['color'] = clean_color(df.color)

    columns_to_category = ['color', 'class']
    other_columns = [col for col in df.columns if col not in columns_to_category]
    
    transformer = ColumnTransformer(
        [
            ('str_to_cat', build_categorical_pipeline(), columns_to_category),
            ('other_cat', 'passthrough', other_columns),
        ]
    )
    
    # df = transformer.fit_transform(X=df, y=None)
    for col in columns_to_category:
        df[col] = pd.Categorical(df[col])
        df[col] = df[col].cat.codes

    return df