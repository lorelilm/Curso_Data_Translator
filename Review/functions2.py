import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def get_final_data():
    X_train_raw, X_test_raw, y_train, y_test = get_raw_data()
    X_train_raw_col_fix = fix_col_names(X_train_raw)
    X_test_raw_col_fix = fix_col_names(X_test_raw)
    cols = ['p_class', 'sex', 'age', 'sib_sp', 'parch', 'fare', 'embarked']
    clean = Cleaner(cols)
    clean.fit(X_train_raw_col_fix)
    X_train = clean.transform(X_train_raw_col_fix)
    X_test = clean.transform(X_test_raw_col_fix)
    return X_train, X_test, y_train, y_test

def get_raw_data():
    df = pd.read_csv('data/titanic.csv')
    y = df.Survived
    X = df.drop('Survived', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    return X_train, X_test, y_train.values, y_test.values

def fix_col_names(df):
    df = df.copy()
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    return df

class Cleaner:
    def __init__(self, cols_to_keep):
        self.cols_to_keep = cols_to_keep

    def fit(self, X_train):
        self.mean_age = X_train.age.mean()
        self.mode_embarked = X_train.embarked.mode()[0]
        temp_df = X_train.copy()
        temp_df.embarked = temp_df.embarked.fillna(self.mode_embarked)
        self.enc = OneHotEncoder(drop='first', sparse=False, handle_unknown='ignore')
        self.enc.fit(temp_df[['embarked']])

    def transform(self, X_any):
        df = X_any[self.cols_to_keep].copy()
        df = df.reset_index(drop=True)
        df.age = df.age.fillna(self.mean_age)
        df['is_male'] = df.sex == 'male'
        df.embarked = df.embarked.fillna(self.mode_embarked)
        emb_df = pd.DataFrame(self.enc.transform(df[['embarked']]), columns=self.enc.get_feature_names_out())
        df = df.drop(['sex', 'embarked'], axis=1)
        return pd.concat([df, emb_df], axis=1)
