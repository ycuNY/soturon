import numpy as np
import pandas as pd
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

label = "m/z"
int = "Intensity"

Path = st.sidebar.file_uploader('Excel')
if Path is not None:
    Data = pd.ExcelFile(Path)
    Sheet_names = Data.sheet_names
    total = st.sidebar.radio(label="total value", options=(1, 100))

    df_list = []
    for i in range(len(Sheet_names)):
        df_list.append("BOX" + str(i + 1))

    DF_list = []
    count = 0
    for Sheet_name, df in zip(Sheet_names, df_list):
        count = count + 1
        df = pd.read_excel(Path, sheet_name=Sheet_name)
        df = df.groupby(label).sum()
        df = df / df.sum() * total
        df = df.set_axis(["BOX" + str(count)], axis=1)
        DF_list.append(df)

        if count == 1:
            DF = df
        else:
            DF = pd.concat([DF, df], axis=1)

    DF["mean"] = DF.mean(axis=1)
    DF["std"] = DF.std(axis=1)
    st.write(DF)