def save_csv(df, filename):
    df.to_csv(filename, index=False)

def save_postgres(df, table, engine):
    df.to_sql(table, engine, if_exists="replace", index=False)