import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("speeddating.csv")


def data_inspect(df):
    print(df.head)
    print(df.describe())


def substr_b(x):
    return x[2:(-1)]

def syntaxcorr(df):
    for col in df:
        if isinstance(df[col][0], str) and (df[col][0])[0:2] == "b'" and (df[col][0])[-1] == "'":
            df[col] = df[col].apply(lambda x: substr_b(x))


def set_one_zero(x):
    y = 0
    if x > 0:
        y = 1
    return y


def norm_met(df):
    df['met'] = df['met'].apply(lambda x: set_one_zero(x))

def mm_scaler(df, field, ran):
    avg = df[field].mean()
    df[field].fillna(value=avg)
    scaler = MinMaxScaler()
    scaler.fit(np.array(df[field]).reshape(-1, 1))
    df[field] = scaler.transform(np.array(df[field]).reshape(-1, 1))
    df[field] = df[field] * ran
    df[field] = round(df[field], 0).astype('float32')


def to_title(st):
    return st.title()


def uniform_uppercase(df, field):
    df[field] = df[field].apply(lambda x: to_title(x))


def update_der1(el1):
    set1 = ["[0-5]", "[6-8]", "[9-10]"]
    if 0 <= el1 < 6:
        dest = set1[0]
    elif 6 <= el1 < 9:
        dest = set1[1]
    elif el1 >= 9:
        dest = set1[2]
    else:
        dest = set1[0]
    # print(el1, dest)
    return dest


def app_der1(df, f1, f2):
    df[f2] = df[f1].apply(lambda x: update_der1(x))


to_upper_fields = ['field']
to_norm_fields = ['attractive_o', 'funny_o', 'gaming', 'reading']
to_upd_fields = ['d_attractive_o', 'd_funny_o', 'd_gaming', 'd_reading']

data_inspect(data)

syntaxcorr(data)
norm_met(data)
for i in to_norm_fields:
    mm_scaler(data, i, 10)
for i in to_upper_fields:
    uniform_uppercase(data, i)

print(data['attractive_o'].dtypes)
for i in range(len(to_norm_fields)):
    app_der1(data, to_norm_fields[i], to_upd_fields[i])

data_inspect(data)
print(data.dtypes)

data.to_csv('speeddating-v1.csv', index=False)
