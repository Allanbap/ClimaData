from extract import get_weather_data
from transform import current_to_dataframe
from load import save_csv, save_postgres
from config import URL, POSTGRES_CONN
from sqlalchemy import create_engine
import streamlit as st
import pandas as pd


data = get_weather_data(URL)
df = current_to_dataframe(data)

save_csv(df, "clima.csv")

engine = create_engine(POSTGRES_CONN)
save_postgres(df, "clima", engine)
df = pd.read_sql("SELECT * FROM clima", engine)
engine.dispose()
print("Dados recebidos no banco na tabela clima.")

st.title("Dashboard de Clima")
st.write("Visualização dos dados de clima coletados:")

st.dataframe(df)
