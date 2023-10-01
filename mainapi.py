from flask import Flask, render_template
import pandas as pd
import numpy as np


app=Flask("__name__")
dset = pd.read_csv("dataset/stations.txt", skiprows=17)
dset=dset[['STAID','STANAME                                 ']]

@app.route('/')
def home():
    return render_template("myapi.html", data=dset.to_html())
@app.route("/api/v1/<station>/<date>/")

def hi(station, date):
    id = "TG_STAID"
    filepath = "dataset/" + id + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    df['TG'] = df['   TG'].mask(df['   TG'] == -9999, np.nan)
    temperature = df.loc[df['    DATE']== date]['TG'].squeeze()/10
    apidata = {"station": station, "date": date, "temperature": temperature}
    return apidata

@app.route("/api/v1/<station>/")
def hello(station):
    id = "TG_STAID"
    filepath = "dataset/" + id + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20, parse_dates=['    DATE'])
    df['TG'] = df['   TG'].mask(df['   TG'] == -9999, np.nan)/10
    rec = df[['    DATE', 'TG']].to_dict(orient = "records")
    return rec

@app.route("/api/v1/yearly/<station>/<year>/")
def yearly(station, year):
    id = "TG_STAID"
    filepath = "dataset/" + id + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath, skiprows=20)
    df['TG'] = df['   TG'].mask(df['   TG'] == -9999, np.nan)/10
    df['    DATE']=df['    DATE'].values.astype(str)
    rec = df.loc[df['    DATE'].str.startswith(str(year))].to_dict(orient = "records")
    return rec


if __name__ == "__main__":
    app.run(debug=True, port= 5001)