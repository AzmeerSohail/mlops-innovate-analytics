def clean_data(df):
    df = df.dropna()
    df = df[df["age"] > 0]
    return df
