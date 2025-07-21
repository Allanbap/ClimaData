import pandas as pd

def current_to_dataframe(data):
    current = data['current']
    return pd.DataFrame([current])