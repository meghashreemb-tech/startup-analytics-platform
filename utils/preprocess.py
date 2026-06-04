def preprocess_data(df):

    df.columns = df.columns.str.strip()

    df.drop_duplicates(inplace=True)

    df.fillna(0, inplace=True)

    return df
